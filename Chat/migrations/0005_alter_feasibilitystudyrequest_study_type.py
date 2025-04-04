# Generated by Django 5.0.1 on 2024-06-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0004_studytype_alter_feasibilitystudyrequest_study_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feasibilitystudyrequest',
            name='study_type',
            field=models.CharField(choices=[('market_analysis', 'تحليل السوق'), ('financial_analysis', 'التحليل المالي'), ('risk_assessment', 'تقييم المخاطر')], default=('market_analysis', 'financial_analysis', 'risk_assessment'), max_length=50),
        ),
    ]
