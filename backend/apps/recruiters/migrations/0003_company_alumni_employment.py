# Generated manually for company-alumni employment relationships.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("alumni", "0003_alumni_verification_workflow"),
        ("recruiters", "0002_company_review_and_workflow_audit"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyAlumniEmployment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("designation", models.CharField(max_length=150)),
                ("employment_status", models.CharField(
                    choices=[("CURRENT", "Current"), ("FORMER", "Former")],
                    default="CURRENT", max_length=10,
                )),
                ("verification_status", models.CharField(
                    choices=[("PENDING", "Pending"), ("VERIFIED", "Verified"), ("REJECTED", "Rejected")],
                    default="PENDING", max_length=10,
                )),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("verified_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("alumni", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="employment_relationships", to="alumni.alumniprofile",
                )),
                ("company", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="alumni_employments", to="recruiters.company",
                )),
                ("verified_by", models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="verified_alumni_employments", to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "db_table": "company_alumni_employments",
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["company", "employment_status", "verification_status"], name="company_alumni_status_idx"),
                    models.Index(fields=["alumni", "verification_status"], name="alumni_employment_verify_idx"),
                ],
                "constraints": [
                    models.UniqueConstraint(fields=("company", "alumni", "start_date"), name="uniq_company_alumni_start"),
                    models.CheckConstraint(
                        condition=models.Q(("employment_status", "FORMER"), ("end_date__isnull", True), _connector="OR"),
                        name="current_employment_no_end_date",
                    ),
                ],
            },
        ),
    ]
