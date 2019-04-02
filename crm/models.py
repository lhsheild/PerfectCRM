from django.contrib import auth
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager, \
    PermissionDenied
from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(username)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    账户表
    """
    username = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_admin = models.BooleanField(default=False)
    name = models.CharField('名字', max_length=32)
    department = models.ForeignKey('Department', default=None, blank=True, null=True)
    mobile = models.CharField('手机', max_length=32, default=None, blank=True, null=True)
    memo = models.TextField('备注', blank=True, default=None, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super(AbstractUser, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.name


def _user_get_all_permissions(user, obj):
    permissions = set()
    for backend in auth.get_backends():
        if hasattr(backend, "get_all_permissions"):
            permissions.update(backend.get_all_permissions(user, obj))
    return permissions


def _user_has_perm(user, perm, obj):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


def _user_has_module_perms(user, app_label):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_module_perms'):
            continue
        try:
            if backend.has_module_perms(user, app_label):
                return True
        except PermissionDenied:
            return False
    return False


class Customer(models.Model):
    """
    客户信息表
    """
    name = models.CharField(max_length=32, null=True, blank=True, help_text='报名后改为真实姓名')
    qq = models.CharField(max_length=64, unique=True, null=False)
    qq_name = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    source_type = (
        ('referral', '转介绍'), ('qq', 'QQ群'), ('website', '官网'), ('baidu_ads', '百度推广'), ('office_direct', '直接上门'),
        ('WoM', '口碑'), ('public_class', '公开课'), ('website_luffy', '路飞官网'), ('others', '其它'))
    source = models.CharField(choices=source_type, max_length=64, default='qq')
    introduce_from = models.ForeignKey('self', verbose_name='转介绍自学员', blank=True, null=True)
    course_choices = (('LinuxL', 'Linux中高级'), ('PythonFullStack', 'Python高级全栈开发'))
    course = models.MultiSelectField(choices=course_choices, verbose_name='咨询课程')
    class_type_choices = (('fulltime', '脱产班'), ('online', '网络班'), ('weekend', '周末班'))
    class_type = models.CharField('班级类型', max_length=64, choices=class_type_choices, default='fulltime')
    content = models.TextField(verbose_name='咨询详情')
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    consultant = models.ForeignKey('UserProfile')
    memo = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status_choices = ((0, '已报名'), (1, '未报名'),)
    status = models.SmallIntegerField(choices=status_choices, default=1)
    sex_type = (('male', '男'), ('female', '女'))
    sex = models.CharField(choices=sex_type, max_length=16, default='male', blank=True, null=True)
    birthday = models.DateField('出生日期', default=None, help_text='格式yyyy-mm-dd', blank=True, null=True)

    def __str__(self):
        return self.qq

    class Meta:
        verbose_name = '客户表'
        verbose_name_plural = '客户表'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class CustomerFollowUp(models.Model):
    """
    客户跟进表
    """
    customer = models.ForeignKey('Customer')
    content = models.TextField(verbose_name='跟进内容')
    consultant = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now_add=True)
    intention_choices = ((0, '2周内报名'), (1, '1月内报名'), (2, '近期无报名计划'), (3, '已在其它机构报名'), (4, '已报名'), (5, '已拉黑'),)
    intention = models.SmallIntegerField(choices=intention_choices)

    def __str__(self):
        return f'<{self.customer.qq} : {self.intention}>'

    class Meta:
        verbose_name = '客户跟进记录'
        verbose_name_plural = '客户跟进记录'


class Course(models.Model):
    """
    课程表
    """
    name = models.CharField(max_length=64, unique=True)
    price = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField(verbose_name='周期（月）')
    outline = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'


class Branch(models.Model):
    """
    校区
    """
    name = models.CharField(max_length=128, unique=True)
    addr = models.CharField(max_length=128)

    class Meta:
        verbose_name = '校区'
        verbose_name_plural = '校区'


class ClassList(models.Model):
    """
    班级表
    """
    branch = models.ForeignKey("Branch", verbose_name='分校')
    course = models.ForeignKey('Course')
    semester = models.PositiveSmallIntegerField('学期')
    teachers = models.ManyToManyField('UserProfile')
    class_type_choices = ((0, '面授（脱产）'), (1, '面授（周末）'), (2, '网络班'))
    class_type = models.SmallIntegerField(choices=class_type_choices, verbose_name='班级类型')
    start_date = models.DateField(verbose_name='开班日期')
    end_date = models.DateField(verbose_name='结业日期', blank=True, null=True)

    def __str__(self):
        return f'{self.branch}, {self.semester}, {self.course}'

    class Meta:
        unique_together = ('branch', 'course', 'semester')
        verbose_name = '班级'
        verbose_name_plural = '班级'


class CourseRecord(models.Model):
    """
    上课记录表
    """
    from_class = models.ForeignKey("ClassList", verbose_name="班级")
    day_num = models.PositiveSmallIntegerField(verbose_name="第几节（天）")
    teacher = models.ForeignKey('UserProfile')
    has_homework = models.BooleanField(default=True)
    homework_title = models.CharField(max_length=128, blank=True, null=True)
    homework_content = models.TextField(blank=True, null=True)
    outline = models.TextField(verbose_name="本节课大纲")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_class}, {self.day_num}'

    class Meta:
        unique_together = ('from_class', 'day_num')
        verbose_name = '上课记录'
        verbose_name_plural = '上课记录'


class StudyRecord(models.Model):
    """
    学习记录表
    """
    student = models.ForeignKey("Enrollment")
    course_record = models.ForeignKey("CourseRecord")
    attendance_choices = ((0, '已签到'), (1, '迟到'), (2, '缺勤'), (3, '早退'))
    attendance = models.SmallIntegerField(choices=attendance_choices, default=0)
    score_choices = (
        (100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'),
        (-100, 'COPY'), (0, 'N/A'))
    score = models.SmallIntegerField(choices=score_choices)
    memo = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, {self.course_record}, {self.score}'

    class Meta:
        unique_together = ('student', 'course_record')
        verbose_name = '学习记录'
        verbose_name_plural = '学习记录'


class Enrollment(models.Model):
    """
    报名表
    """
    customer = models.ForeignKey("Customer")
    enrolled_class = models.ForeignKey("ClassList", verbose_name="所报班级")
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")
    contract_agree = models.BooleanField(default=False, verbose_name="同意条款")
    contract_approved = models.BooleanField(default=False, verbose_name='已审核')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}  {self.enrolled_class}'

    class Meta:
        unique_together = ('customer', 'enrolled_class')
        verbose_name = '报名表'
        verbose_name_plural = '报名表'


class Payment(models.Model):
    """
    缴费记录
    """
    customer = models.ForeignKey('Customer')
    course = models.ForeignKey('Course', verbose_name='所报课程')
    amount = models.PositiveIntegerField(verbose_name='数额', default=500)
    consultant = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} {self.amount}'

    class Meta:
        verbose_name = '缴费记录'
        verbose_name_plural = '缴费记录'


class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门名称')
    count = models.IntegerField('人数', default=0)

    def __str__(self):
        return f'{self.name}  {self.count}'


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, unique=True)
    menus = models.ManyToManyField('Menu', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = '角色'


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=32)
    url_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = '菜单'
