ModelForm:
----------------------
1. If you're building a database-driven app, chances are you‘ll have forms that map 
closely to Django models
2. In this case, it would be redundant to define the field types in your form, because 
you‘ve already defined the fields in your model.
3. so in order to avoid such difficulties django has provided one helper class
ModelForm which is responsible for creating forms based on models
4. Each and every form class must be inherited from ModelForm class of forms module


Advantages of ModelForms:
-------------------------
1. Mapping of model fields with form fields can be done easily
2. Reduces Code redundancy
3. Saving of the collected data from front-end can be done easily just by using Save() 
method
4. Customization of Model fields can be done easily

Attributes of Meta class:
----------------------------------

model:
------------

It is used for representing ModelName from which we need to create form

syntax: model = Modelname

fields:
-----------------------
 It is used to specify which all the Model attributes are to be represented as form 
input input elements.

Fields values can be represented in list or tuple
syntax: fields = value
fields='__all__' ------>takes all attributes of model
fields=['attriute1','attriute2'......'attriuten']


exclude:
------------------
It is used to specify which all the Model attributes are not to be represented as form 
input input elements.

fields values can be represented in list or tuple
syntax: exclude==['attriute1','attriute2'......'attriuten']


how to create ModelForms:
-------------------------
step 1 ) create model first inside models.py

step 2 ) create a form which inherit from forms.Modelform
		
		ex:
		class EmployeeForm(forms.ModelForm):

step 3) create a Meta class(innerclass) inside the form class
		
		ex:
		class EmployeeForm(forms.ModelForm):
    			class Meta:
step 4) meta class contains some fields
	
	model,fields,exclude

step 5) model field in meta should contain ref of Model

step 6) fields in meta class should contain either 

		fields='__all__'
		 # fields=['fieldname1','fieldname2',.....'fieldNamen]
step 7) u can use exclude to avoid particular fields


		class EmployeeForm(forms.ModelForm):
    			class Meta:
        			model=EmployeeModel
        			fields='__all__'
        			# fields=['fieldname1','fieldname2',.....'fieldNamen]
        			#fields=['name']
        			#exclude=['age']
