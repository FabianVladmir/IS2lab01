# Generated by Django 2.2.24 on 2021-07-23 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0121_auto_20210723_0747'),
    ]

    operations = [
         migrations.RunSQL(
            sql='''
              CREATE TRIGGER vector_column_trigger
              BEFORE INSERT OR UPDATE OF title, description, vector_column
              ON grants_grant
              FOR EACH ROW EXECUTE PROCEDURE
              tsvector_update_trigger(
                vector_column, 'pg_catalog.english', title, description
              );
              UPDATE grants_grant SET vector_column = NULL;
            ''',

            reverse_sql = '''
              DROP TRIGGER IF EXISTS vector_column_trigger
              ON grants_grant;
            '''
        ),
    ]
