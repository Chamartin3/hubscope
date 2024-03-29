from django.urls import path
from  hubscope.accounts import views

urlpatterns = [
      path("list/", views.UserList.as_view(), name="accounts-list"),
      path("grouplist/", views.GroupList.as_view(), name="accounts-groups"),
      path("registration/", views.UserRegistration.as_view(), name="accounts-registration"),
      path("info/<int:pk>/", views.UserInformation.as_view(), name="accounts-information"),
      path("delete/<int:pk>/", views.UserDelete.as_view(), name="accounts-delete"),

      path("password/<int:pk>/", views.ChangePassword.as_view(), name="accounts-change_password"),
      path("groups/<int:pk>/", views.ChangeGroup.as_view(), name="accounts-change_group"),
      path("perms/<int:pk>/", views.UserStatusPermisions.as_view(), name="accounts-permisions"),
      path("search/", views.UserSearch.as_view(), name="accounts-search"),

      path("auth", views.Auth.as_view(), name="auth"),
      # path("auth", views.Login.as_view(), name="login"),
      # TODO: Token based autentication, password recuperation by Token /

  ]
