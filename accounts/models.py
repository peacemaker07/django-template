from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	""" セクション """
	SECTION_CHOICES = (
		(1, 'フロントセクション'),
		(2, 'バックエンドセクション'),
		(3, '総務・経理セクション'),
		(4, 'なし'),
	)

	""" 役職 """
	position_CHOICES = (
		(1, '担当'),
		(2, '常務取締役'),
		(3, '取締役 統括'),
		(4, 'アドバイザー'),
		(5, 'セクションディレクター'),
		(6, 'エキスパート'),
	)

	section = models.IntegerField(verbose_name='セクション', choices=SECTION_CHOICES, default=1, blank=True)
	position = models.IntegerField(verbose_name='役職', choices=position_CHOICES, default=1, blank=True)

CustomUser._meta.get_field('first_name').null = False
CustomUser._meta.get_field('first_name').blank = False
CustomUser._meta.get_field('last_name').null = False
CustomUser._meta.get_field('last_name').blank = False
