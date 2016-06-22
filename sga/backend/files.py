import os
from io import BytesIO
from zipfile import ZipFile

from django.http import HttpResponse


def serve_zip_file(filepaths, zipname="zipfile"):
    # Create zip file in memory StringIO()
    s = BytesIO()
    with ZipFile(s, "w") as z:
        for filepath in filepaths:
            filedir, filename = os.path.split(filepath)
            z.write(filepath, arcname=os.path.join(zipname, filename))
    # Serve zip file in response
    resp = HttpResponse(s.getvalue(), content_type="application/zip")
    resp["Content-Disposition"] = "attachment; filename={zipname}.zip".format(zipname=zipname)
    return resp

def student_submission_file_path(instance, filename):
    return "student-uploads/{course_id}/{last_name}_{first_name}-{assignment_name}{extension}".format(
        course_id=instance.assignment.course.edx_id,
        last_name=instance.student.last_name,
        first_name=instance.student.first_name,
        assignment_name=instance.assignment.name,
        extension=os.path.splitext(filename)[-1]
    )

def grader_submission_file_path(instance, filename):
    return "grader-uploads/{course_id}/{last_name}_{first_name}-{assignment_name}{extension}".format(
        course_id=instance.assignment.course.edx_id,
        last_name=instance.student.last_name,
        first_name=instance.student.first_name,
        assignment_name=instance.assignment.name,
        extension=os.path.splitext(filename)[-1]
    )