from __future__ import unicode_literals
from django.db import models
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')


class UserManager(models.Manager):
########################################## REGISTRATION VALIDATION ##########################################
    def basic_validator(self,postData):
        errors= {}
        if len(postData['first_name'])<2:
            errors['first_name']='first name needed'
        if len(postData['last_name'])<2:
            errors['last_name']='last name needed'
        if re.search ("[0-9]", postData['password']) is None:
            errors ['password']='password must contain a number'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='email required'
        if len(postData['password'])<8:
            errors['password']='password to short'
        if re.search('[A-Z]',postData['password']) is None:
            errors['password']='password needs one capital letter'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='email required'
        if postData['password']!=postData['conpassword']:
            errors['password']="passwords dont match"
        return errors



########################################## LOGIN VALIDATION ##########################################
    def login_validator(self,postData):
        is_valid={'errors':{},
                'status':True}
                #creates an Dictionary with to Dictionarys one being a key with empty value taht we pass later in the code
                #the second one is saying key is status and value is true 
        try:
            user = User.objects.get(email=postData['loginEmail'])
            #trying to see if the email passed in the form matches whats in the database 
            if user.password == postData['loginPassword']: #if the password of the user we're currently working with is a match 
                return is_valid #then we return the is valid Dictionary and there are no errors and the status is true 
            else: #if thats not the case then do this code below 
                is_valid['errors']['password'] = "Password is invalid" # the Dictionary is valid Dictionary 1 is calling the key of errors and passing the value of password string 
                is_valid['status'] = False #changing the value of status from True to False 
                return is_valid # return is valid with the new values 
        except:
            is_valid['errors']['email'] = "Invalid email" #if the try fails return the is valid Dictionary with the errors key having a vlue of email string response 
            is_valid['status'] = False # and passing the second Dictionary and updating its value to False 
            return is_valid # return the is valid Dictionarys with their new values 






class User(models.Model):
    # id
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
