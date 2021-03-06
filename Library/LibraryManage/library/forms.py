from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Username",
            'autofocus': ''
        }))
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Password"
        }))
    # captcha = CaptchaField(label="验证码", widget=forms.TextInput(attrs={'class':'form-control'}))
    # captcha = CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('general_user', "普通用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password1 = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    password2 = forms.CharField(
        label="确认密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    # role = forms.ChoiceField(label="角色", choices=roles)
    # captcha = CaptchaField(label="验证码")


class addUserForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('general_user', "普通用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    role = forms.ChoiceField(
        label="注册身份",
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))


class deleteUserForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('general_user', "普通用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    id_number = forms.IntegerField(
        label="会员卡号",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    role = forms.ChoiceField(
        label="注册身份",
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))


class updateUserForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('general_user', "普通用户"),
        ('admin', "管理员"),
    )
    id_number = forms.IntegerField(
        label="会员卡号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    role = forms.ChoiceField(
        label="注册身份",
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))


class getUserForm(forms.Form):
    gender = (
        (None, "无要求"),
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        (None, "无要求"),
        ('general_user', "普通用户"),
        ('admin', "管理员"),
    )
    id_number = forms.IntegerField(
        label="会员卡号",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    username = forms.CharField(
        label="用户名",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        required=False,
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))
    sex = forms.ChoiceField(
        label="性别",
        required=False,
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    role = forms.ChoiceField(
        label="注册身份",
        required=False,
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))


class addBookForm(forms.Form):
    author = forms.CharField(
        label="作者",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.IntegerField(
        label="ISBN号",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))

    book_count = forms.IntegerField(
        label="馆藏数量",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "馆藏数量",
        }))

    book_remark = forms.CharField(
        label="书籍简介",
        max_length=1024,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书籍简介",
        }))


class deleteBookForm(forms.Form):
    author = forms.CharField(
        label="作者(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.CharField(
        label="ISBN号(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))


class updateBookForm(forms.Form):
    author = forms.CharField(
        label="作者(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.CharField(
        label="ISBN号(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社(必填)",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))

    book_count = forms.IntegerField(
        label="馆藏数量(必填)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "馆藏数量",
        }))

    book_remark = forms.CharField(
        label="书籍简介(必填)",
        max_length=1024,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书籍简介",
        }))


class getBookForm(forms.Form):
    author = forms.CharField(
        label="作者",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.CharField(
        label="ISBN号",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))

    book_count = forms.IntegerField(
        label="馆藏数量",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "馆藏数量",
        }))


class addBorrowRecordForm(forms.Form):

    limit_time = forms.IntegerField(
        label="借书截止时间(默认31天)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "借书截止时间",
        }))

    id_number = forms.IntegerField(
        label="会员卡号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "会员卡号",
        }))

    isbn = forms.IntegerField(
        label="ISBN号(必填)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))


class deleteBorrowRecordForm(forms.Form):
    isbn = forms.IntegerField(
        label="ISBN号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    id_number = forms.IntegerField(
        label="会员卡号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "会员卡号",
        }))


class updateBorrowRecordForm(forms.Form):
    limit_time = forms.IntegerField(
        label="借书截止时间(默认31天)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "借书截止时间",
        }))

    id_number = forms.IntegerField(
        label="会员卡号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "会员卡号",
        }))

    isbn = forms.IntegerField(
        label="ISBN号(必填)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))


class getBorrowRecordForm(forms.Form):
    borrow_time = forms.DateTimeField(
        label="借书时间 格式为：2019-06-08 19:55:40",
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': "借书时间",
        }))
    limit_time = forms.IntegerField(
        label="借书截止时间",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "借书截止时间",
        }))

    book_name = forms.CharField(
        label="书名",
        required=False,
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.IntegerField(
        label="ISBN号",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    id_number = forms.IntegerField(
        label="会员卡号(必填)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "会员卡号(必填)",
        }))