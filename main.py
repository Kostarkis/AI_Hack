# -*- coding: utf-8 -*-
import os
from openai import OpenAI
import dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma



dotenv.load_dotenv(dotenv.find_dotenv(".env"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings()

subfolder_path = 'ProjectToBeAnalyzed\Django-School-Management-System'

project_file_tree = "ProjectToBeAnalyzed\n└── Django-School-Management-System\n    ├── manage.py\n    ├── school_app\n    │   ├── __init__.py\n    │   ├── asgi.py\n    │   ├── settings.py\n    │   ├── urls.py\n    │   └── wsgi.py\n    ├── apps\n    │   ├── __init__.py\n    │   ├── corecode\n    │   │   ├── __init__.py\n    │   │   ├── admin.py\n    │   │   ├── apps.py\n    │   │   ├── context_processors.py\n    │   │   ├── forms.py\n    │   │   ├── middleware.py\n    │   │   ├── models.py\n    │   │   ├── signals.py\n    │   │   ├── tests.py\n    │   │   ├── urls.py\n    │   │   ├── views.py\n    │   │   ├── migrations\n    │   │   │   ├── __init__.py\n    │   │   │   ├── 0001_initial.py\n    │   │   │   ├── 0002_auto_20200506_1520.py\n    │   │   │   ├── 0003_auto_20200726_0925.py\n    │   │   │   └── 0004_auto_20201124_0614.py\n    │   │   └── templates\n    │   │       └── corecode\n    │   │           ├── class_list.html\n    │   │           ├── core_confirm_delete.html\n    │   │           ├── current_session.html\n    │   │           ├── form_snippet.html\n    │   │           ├── mgt_form.html\n    │   │           ├── session_list.html\n    │   │           ├── siteconfig.html\n    │   │           ├── subject_list.html\n    │   │           └── term_list.html\n    │   ├── finance\n    │   │   ├── __init__.py\n    │   │   ├── admin.py\n    │   │   ├── apps.py\n    │   │   ├── forms.py\n    │   │   ├── models.py\n    │   │   ├── signals.py\n    │   │   ├── tests.py\n    │   │   ├── urls.py\n    │   │   ├── views.py\n    │   │   ├── migrations\n    │   │   │   ├── __init__.py\n    │   │   │   └── 0001_initial.py\n    │   │   └── templates\n    │   │       └── finance\n    │   │           ├── bulk_invoice.html\n    │   │           ├── invoice_confirm_delete.html\n    │   │           ├── invoice_detail.html\n    │   │           ├── invoice_form.html\n    │   │           ├── invoice_list.html\n    │   │           └── receipt_form.html\n    │   ├── result\n    │   │   ├── __init__.py\n    │   │   ├── admin.py\n    │   │   ├── apps.py\n    │   │   ├── forms.py\n    │   │   ├── models.py\n    │   │   ├── tests.py\n    │   │   ├── urls.py\n    │   │   ├── utils.py\n    │   │   ├── views.py\n    │   │   ├── migrations\n    │   │   │   ├── __init__.py\n    │   │   │   └── 0001_initial.py\n    │   │   └── templates\n    │   │       └── result\n    │   │           ├── all_results.html\n    │   │           ├── create_result.html\n    │   │           ├── create_result_page2.html\n    │   │           └── edit_results.html\n    │   ├── staffs\n    │   │   ├── __init__.py\n    │   │   ├── admin.py\n    │   │   ├── apps.py\n    │   │   ├── models.py\n    │   │   ├── tests.py\n    │   │   ├── urls.py\n    │   │   ├── views.py\n    │   │   ├── migrations\n    │   │   │   ├── __init__.py\n    │   │   │   ├── 0001_initial.py\n    │   │   │   └── 0002_auto_20201124_0614.py\n    │   │   └── templates\n    │   │       └── staffs\n    │   │           ├── staff_confirm_delete.html\n    │   │           ├── staff_detail.html\n    │   │           ├── staff_form.html\n    │   │           └── staff_list.html\n    │   └── students\n    │       ├── __init__.py\n    │       ├── admin.py\n    │       ├── apps.py\n    │       ├── models.py\n    │       ├── signals.py\n    │       ├── tests.py\n    │       ├── urls.py\n    │       ├── views.py\n    │       ├── migrations\n    │       │   ├── __init__.py\n    │       │   ├── 0001_initial.py\n    │       │   └── 0002_auto_20201124_0614.py\n    │       └── templates\n    │           └── students\n    │               ├── students_upload.html\n    │               ├── student_confirm_delete.html\n    │               ├── student_detail.html\n    │               ├── student_form.html\n    │               └── student_list.html\n    ├── static\n    │   └── dist\n    │       ├── css\n    │       │   ├── adminlte.css\n    │       │   ├── adminlte.css.map\n    │       │   ├── adminlte.min.css\n    │       │   ├── adminlte.min.css.map\n    │       │   └── login-page.css\n    │       └── js\n    │           ├── adminlte.js\n    │           ├── adminlte.js.map\n    │           ├── adminlte.min.js\n    │           ├── adminlte.min.js.map\n    │           ├── custom.js\n    │           ├── demo.js\n    │           ├── jquery.formset.js\n    │           └── pages\n    │               ├── dashboard.js\n    │               ├── dashboard2.js\n    │               └── dashboard3.js\n    └── templates\n        ├── base.html\n        ├── index.html\n        ├── paginator.html\n        └── registration\n            └── login.html"

system_prompt = "Code fragmentation process example:\n\nFOR THE GIVEN CODE:\n\nfrom django import forms\nfrom django.forms import ModelForm, modelformset_factory\n\nfrom .models import (\n    AcademicSession,\n    AcademicTerm,\n    SiteConfig,\n    StudentClass,\n    Subject,\n)\n\nSiteConfigForm = modelformset_factory(\n    SiteConfig,\n    fields=(\n        \"key\",\n        \"value\",\n    ),\n    extra=0,\n)\n\n\nclass AcademicSessionForm(ModelForm):\n    prefix = \"Academic Session\"\n\n    class Meta:\n        model = AcademicSession\n        fields = [\"name\", \"current\"]\n\n\nclass AcademicTermForm(ModelForm):\n    prefix = \"Academic Term\"\n\n    class Meta:\n        model = AcademicTerm\n        fields = [\"name\", \"current\"]\n\n\nclass SubjectForm(ModelForm):\n    prefix = \"Subject\"\n\n    class Meta:\n        model = Subject\n        fields = [\"name\"]\n\n\nclass StudentClassForm(ModelForm):\n    prefix = \"Class\"\n\n    class Meta:\n        model = StudentClass\n        fields = [\"name\"]\n\n\nclass CurrentSessionForm(forms.Form):\n    current_session = forms.ModelChoiceField(\n        queryset=AcademicSession.objects.all(),\n        help_text='Click <a href=\"/session/create/?next=current-session/\">here</a> to add new session',\n    )\n    current_term = forms.ModelChoiceField(\n        queryset=AcademicTerm.objects.all(),\n        help_text='Click <a href=\"/term/create/?next=current-session/\">here</a> to add new term',\n    )\n\n###\nFOLLOWING FRAGMENTATION IS EXPECTED:\n\n##FRAGMENT_0\n\nSiteConfigForm = modelformset_factory(\n    SiteConfig,\n    fields=(\n        \"key\",\n        \"value\",\n    ),\n    extra=0,\n)\n\n\n##FRAGMENT_1\n\nclass AcademicSessionForm(ModelForm):\n    prefix = \"Academic Session\"\n\n    class Meta:\n        model = AcademicSession\n        fields = [\"name\", \"current\"]\n\nDEPENDECIES:\nAcademicSessionForm.Meta\n\n##FRAGMENT_2\n\n\nclass AcademicTermForm(ModelForm):\n    prefix = \"Academic Term\"\n\n    class Meta:\n        model = AcademicTerm\n        fields = [\"name\", \"current\"]\n\nDEPENDECIES:\nAcademicTermForm.Meta\n\n##FRAGMENT_3\n\nclass SubjectForm(ModelForm):\n    prefix = \"Subject\"\n\n    class Meta:\n        model = Subject\n        fields = [\"name\"]\n\nDEPENDECIES:\nSubjectForm.Meta\n\n##FRAGMENT_6\nclass SubjectForm.Meta:\n        model = Subject\n        fields = [\"name\"]\n\n\n##FRAGMENT_4\n\nclass StudentClassForm(ModelForm):\n    prefix = \"Class\"\n\n    class Meta:\n        model = StudentClass\n        fields = [\"name\"]\n\nDEPENDENCIES\n\n##FRAGMENT_5\n\nclass CurrentSessionForm(forms.Form):\n    current_session = forms.ModelChoiceField(\n        queryset=AcademicSession.objects.all(),\n        help_text='Click <a href=\"/session/create/?next=current-session/\">here</a> to add new session',\n    )\n    current_term = forms.ModelChoiceField(\n        queryset=AcademicTerm.objects.all(),\n        help_text='Click <a href=\"/term/create/?next=current-session/\">here</a> to add new term',\n    )\nDEPENDENCIES:\nforms.ModelChoiceField, AcademicSession.objects, AcademicTerm.objects"


def main():
    for root, dirs, files in os.walk(subfolder_path):
        for file in files:
            if file.startswith('.'):
                continue
            if (root.find('\.') != -1):
                continue
            file_path = os.path.join(root, file)

            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read()
                    print(f"File: {file_path}")
                    # print(content)

                    completion = client.chat.completions.create(
                        model="ft:gpt-3.5-turbo-1106:project-orion::8UEe6imY",
                        temperature=0.3,
                        top_p=0.99,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user",
                             "content": "Based on provided above code fragmentation process example, please fragment the following code with the same approach:\n\n" + content + "\n\n###\nDo not include any additional comments or explanations\nI repeat, please fragment above code with the same approach"},
                        ]
                    )

                    completion_response = completion.choices[0].message.content
                    print(completion_response)
                    print()
                    print()
                    breakIf = False
                    while (not breakIf):
                        if (completion_response.find("##FRAGMENT_") != -1):
                            print("GOOD0")
                            itera = 11
                            while(completion_response[itera]!=' ' or completion_response[itera]!='\\'):
                                itera += 1
                            print("GOOD1")
                            completion_response = completion_response[itera-1:completion_response.__len__()-1]
                            this_code_chunk = completion_response[0:completion_response.find("##FRAGMENT_")]
                            completion_response = completion_response[completion_response.find("##FRAGMENT_"):completion_response.__len__()-1]
                            print("GOOD2")
                            #TODO
                            #emmbedding_result =
                            #chroma = Chroma.from_document(embeddings, this_code_chunk)
                            #chroma.save("chroma")

                            dependencies_text = this_code_chunk[this_code_chunk.find("DEPENDENCIES")+12: this_code_chunk.__len__()-1]
                            this_code_chunk = this_code_chunk[0 : this_code_chunk.find("DEPENDENCIES")]
                            this_code_chunk = this_code_chunk.strip()
                            dependencies_text = dependencies_text.strip()
                            dependencies_list = dependencies_text.split(", ")
                            print("GOOD3")

                            res = {
                                "code_chunk": this_code_chunk,
                                "dependencies": dependencies_list,
                                #"embedding":
                            }
                            print(res)
                        else:
                            breakIf = True

            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    print(f'Hi there')


if __name__ == '__main__':
    main()
