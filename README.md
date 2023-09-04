This is a Candidate directory app developed using Django Rest Framework. Created CRUD operations using REST APIs.

Getting Started

1) Run the project using python manage.py runserver and you should see the default success page provided by Django at http://127.0.0.1:8000/api/
2) http://127.0.0.1:8000/admin/ - This is Admin path
   Admin Credentials : Username = ragavi , Password : Ragavi1996##
   
Creating an App
1) Created a folder with the app name in candidateapp.

CRUD Operations API :

1) To Retrive all candidates details

   Method : GET
   API :  http://127.0.0.1:8000/api/candidates/
   Response : 200 OK
            [
            {
            "id": 1,
            "first_name": "Ragavi",
            "last_name": "Mohanraj",
            "email": "mohanrajrag10@gmail.com",
            "recruiter_alert": "Indeed",
            "role": "1",
            "contact_no_primary": "9500913767",
            "contact_no_alternate": "8883340430",
            "years_of_experience": "4.00",
            "current_employer": "Infinit Solutions",
            "current_designation": "Junior Developer",
            "current_monthly_salary": 500000,
            "expected_monthly_salary": 80000,
            "notice_period": "30 days",
            "photo_path": "/images/1722234565.JPEG",
            "resume_path": "/files/u6pevrfoac2ua6zvigrgefyc3h9eraf.pdf",
            "login_time": "2023-09-01T09:25:09Z",
            "logout_time": "2023-09-18T18:00:00Z",
            "ip_address": "10.0.0.0",
            "geo_location": "TN",
            "created_date": "2023-09-03T15:26:23Z",
            "created_by": null,
            "modified_date": "2023-09-03T15:26:26Z",
            "modified_by": null,
            "status": 1,
            "event": 2,
            "job_position": 1,
            "persona": 1,
            "screening_mode": 1,
            "gender": 1,
            "marital_status": 1,
            "employee_directory": 1,
            "city": 1,
            "experience_level": 1,
            "educational_level": 1,
            "equ_qualification": 1,
            "equ_specialization": 1,
            "source": 1,
            "source_type": 3,
            "reason_for_change": 1
            },
            {
            "id": 2,
            "first_name": "Priya",
            "last_name": "Selvaraj",
            "email": "priyas@gmail.com",
            "recruiter_alert": "yes",
            "role": "1",
            "contact_no_primary": "9123245672",
            "contact_no_alternate": "9500913767",
            "years_of_experience": "5.00",
            "current_employer": "Infinit Solutions",
            "current_designation": "Junior Developer",
            "current_monthly_salary": 30000,
            "expected_monthly_salary": 70000,
            "notice_period": "30 days",
            "photo_path": null,
            "resume_path": null,
            "login_time": "2023-09-04T02:51:51Z",
            "logout_time": "2023-09-04T21:51:53Z",
            "ip_address": "18.144.32.91",
            "geo_location": "Chennai",
            "created_date": null,
            "created_by": null,
            "modified_date": null,
            "modified_by": null,
            "status": 1,
            "event": 1,
            "job_position": 1,
            "persona": 1,
            "screening_mode": 1,
            "gender": 1,
            "marital_status": 1,
            "employee_directory": 1,
            "city": 1,
            "experience_level": 1,
            "educational_level": 2,
            "equ_qualification": 1,
            "equ_specialization": 1,
            "source": 1,
            "source_type": 2,
            "reason_for_change": 1
            }
   ]

2) Retreive candidate details by candidate ID
   Method : GET
   API : http://127.0.0.1:8000/api/candidates/2/
   Response : 200 OK
   {
    "id": 2,
    "first_name": "Priya",
    "last_name": "Selvaraj",
    "email": "priyas@gmail.com",
    "recruiter_alert": "yes",
    "role": "1",
    "contact_no_primary": "9123245672",
    "contact_no_alternate": "9500913767",
    "years_of_experience": "5.00",
    "current_employer": "Infinit Solutions",
    "current_designation": "Junior Developer",
    "current_monthly_salary": 30000,
    "expected_monthly_salary": 70000,
    "notice_period": "30 days",
    "photo_path": null,
    "resume_path": null,
    "login_time": "2023-09-04T02:51:51Z",
    "logout_time": "2023-09-04T21:51:53Z",
    "ip_address": "18.144.32.91",
    "geo_location": "Chennai",
    "created_date": null,
    "created_by": null,
    "modified_date": null,
    "modified_by": null,
    "status": 1,
    "event": 1,
    "job_position": 1,
    "persona": 1,
    "screening_mode": 1,
    "gender": 1,
    "marital_status": 1,
    "employee_directory": 1,
    "city": 1,
    "experience_level": 1,
    "educational_level": 2,
    "equ_qualification": 1,
    "equ_specialization": 1,
    "source": 1,
    "source_type": 2,
    "reason_for_change": 1
}
   
 3) Create new Candidate Directory

   Method : POST
   API : http://127.0.0.1:8000/api/create/
   data :
         {"first_name": "Sathya",
        "last_name": "Prakash",
        "email": "sathyam@gmail.com",
        "recruiter_alert": "Indeed",
        "role": "1",
        "contact_no_primary": "9500913767",
        "contact_no_alternate": "8883340430",
        "years_of_experience": "4.00",
        "current_employer": "Infinit Solutions",
        "current_designation": "Junior Developer",
        "current_monthly_salary": 500000,
        "expected_monthly_salary": 80000,
        "notice_period": "30 days",
        "photo_path": null,
        "resume_path": null,
        "login_time": "2023-09-01T09:25:09Z",
        "logout_time": "2023-09-18T18:00:00Z",
        "ip_address": "10.0.0.0",
        "geo_location": "TN"}

   Response : 200 OK

   {
    "id": 6,
    "first_name": "Sathya",
    "last_name": "Prakash",
    "email": "sathyam@gmail.com",
    "recruiter_alert": "Indeed",
    "role": "1",
    "contact_no_primary": "9500913767",
    "contact_no_alternate": "8883340430",
    "years_of_experience": "4.00",
    "current_employer": "Infinit Solutions",
    "current_designation": "Junior Developer",
    "current_monthly_salary": 500000,
    "expected_monthly_salary": 80000,
    "notice_period": "30 days",
    "photo_path": null,
    "resume_path": null,
    "login_time": "2023-09-01T09:25:09Z",
    "logout_time": "2023-09-18T18:00:00Z",
    "ip_address": "10.0.0.0",
    "geo_location": "TN",
    "created_date": "2023-09-04T03:10:01.276428Z",
    "created_by": null,
    "modified_date": "2023-09-04T03:10:01.276428Z",
    "modified_by": null,
    "status": 1,
    "event": null,
    "job_position": null,
    "persona": null,
    "screening_mode": null,
    "gender": null,
    "marital_status": null,
    "employee_directory": null,
    "city": null,
    "experience_level": null,
    "educational_level": null,
    "equ_qualification": null,
    "equ_specialization": null,
    "source": null,
    "source_type": null,
    "reason_for_change": null
}

4) Update existing Candidate

   Method : PUT
   API : http://127.0.0.1:8000/api/update/2/
   data :

   {
    "id": 2,
    "first_name": "Priyanka",
    "last_name": "Selvaraj",
    "email": "priyas@gmail.com",
    "recruiter_alert": "yes",
    "role": "1",
    "contact_no_primary": "9123245672",
    "contact_no_alternate": "9500913767",
    "years_of_experience": "5.00",
    "current_employer": "Infinit Solutions",
    "current_designation": "Junior Developer",
    "current_monthly_salary": 30000,
    "expected_monthly_salary": 70000,
    "notice_period": "30 days",
    "photo_path": null,
    "resume_path": null,
    "login_time": "2023-09-04T02:51:51Z",
    "logout_time": "2023-09-04T21:51:53Z",
    "ip_address": "18.144.32.91",
    "geo_location": "Chennai",
    "created_date": null,
    "created_by": null,
    "modified_date": null,
    "modified_by": null,
    "status": 1,
    "event": 1,
    "job_position": 1,
    "persona": 1,
    "screening_mode": 1,
    "gender": 1,
    "marital_status": 1,
    "employee_directory": 1,
    "city": 1,
    "experience_level": 1,
    "educational_level": 2,
    "equ_qualification": 1,
    "equ_specialization": 1,
    "source": 1,
    "source_type": 2,
    "reason_for_change": 1
}
Response : 200 OK

5) Delete the existing candidate

   Method : DELETE
   API : http://127.0.0.1:8000/api/delete/4/
   Response : 202 Accepted

   
   
      


            
   
    
