from django.shortcuts import render,redirect
from .forms import PatientForm
from .models import Patient00
def patient_list(request):
    context={'liste' : Patient00.objects.all()}
    return render(request,"patiernt/liste.html",context)

def patient_ajouter(request,id=0):
    if request.method=="GET":
       if id ==0:
          form= PatientForm()
       else:
           patient=Patient00.objects.get(pk=id)
           form =PatientForm(instance=patient)
       return render(request,"patiernt/ajouterr.html",{'form':form})
    else:
        if id==0:
           form= PatientForm(request.POST)
        else:
            patient = Patient00.objects.get(pk=id)
            form = PatientForm(request.POST,instance=patient)

        if form.is_valid():
            form.save()
        return redirect('/patient/')
def patient_editer(request):
    return
def patient_delete(request,id):
   patientde = Patient00.objects.get(pk=id)
   patientde.delete()
   return redirect('/patient/')

def patient_contact(request):
    if request.method == "POST":
        email = request.POst['email']
        message= request.Post['message']
        print(email,message)



    return render(request,"patiernt/contact.html")

# Create your views here.
