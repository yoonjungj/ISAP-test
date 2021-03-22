from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


# class AbstractItem(core_models.TimeStampedModel):
#     """ Abstract Item """

#     name = models.CharField(max_length=80)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.name


# class R2toR3KR(AbstractItem):
#     """ R2toR3KR Model Definition """

#     # 기본 정보 입력
#     # 첨부파일 업로드
#     # 처리 후 파일 다운로드
#     # 코멘트 확인
#     name = models.CharField(max_length=140)
#     description = models.TextField()
#     country = CountryField()
#     company = models.CharField(max_length=140)
#     registration_date = models.TimeField()
#     urgent = models.BooleanField(default=False)
#     client = models.ForeignKey(
#         "users.User", related_name="R3", on_delete=models.CASCADE
#     )
#     #request = models.ManyToManyField("Request", related_name="PVA", blank=True)
#     # service_type = models.ForeignKey(
#     #     "ServiceType", related_name="sevices", on_delete=models.SET_NULL, null=True
#     # )

#     class Meta:
#         verbose_name_plural = "R2 to R3(KR)"

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):  # 어딘가에서 모델을 건드릴 때 나타남
#         self.company = str.capitalize(self.company)
#         super().save(*args, **kwargs)  # super는 save()method를 호출


# class R2toR3(AbstractItem):
#     """ R2toR3 Model Definition """

#     class Meta:
#         verbose_name_plural = "R2 to R3"


# class R3errorRepresentor(AbstractItem):
#     """ R3errorRepresentor Model Definition """

#     class Meta:
#         verbose_name_plural = "R3 Error Representor"


# class File(core_models.TimeStampedModel):
#     """ File Model Definition """

#     caption = models.CharField(max_length=80)
#     file = models.ImageField(upload_to="r3_files")
#     R2toR3KR = models.ForeignKey(
#         "R2toR3KR", related_name="files", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.file
