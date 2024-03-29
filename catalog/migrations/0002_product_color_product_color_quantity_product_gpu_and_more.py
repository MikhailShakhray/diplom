# Generated by Django 4.1.7 on 2023-03-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Color',
            field=models.CharField(max_length=255, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='product',
            name='Color_quantity',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество цветов экрана'),
        ),
        migrations.AddField(
            model_name='product',
            name='GPU',
            field=models.CharField(max_length=255, null=True, verbose_name='Графический ускоритель'),
        ),
        migrations.AddField(
            model_name='product',
            name='Headphones_included',
            field=models.CharField(max_length=255, null=True, verbose_name='Наушники в комплекте'),
        ),
        migrations.AddField(
            model_name='product',
            name='Height',
            field=models.CharField(max_length=255, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='product',
            name='Ik_port',
            field=models.CharField(max_length=255, null=True, verbose_name='ИК-порт'),
        ),
        migrations.AddField(
            model_name='product',
            name='Material',
            field=models.CharField(max_length=255, null=True, verbose_name='Материал корпуса'),
        ),
        migrations.AddField(
            model_name='product',
            name='Megapixel_front_camera',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество мегапикселей фронтальной камеры'),
        ),
        migrations.AddField(
            model_name='product',
            name='Megapixel_main_camera',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество мегапикселей основной камеры'),
        ),
        migrations.AddField(
            model_name='product',
            name='Memory',
            field=models.CharField(max_length=255, null=True, verbose_name='Объем встроенной памяти'),
        ),
        migrations.AddField(
            model_name='product',
            name='Memory_card',
            field=models.CharField(max_length=255, null=True, verbose_name='Слот для карты памяти'),
        ),
        migrations.AddField(
            model_name='product',
            name='Model',
            field=models.CharField(max_length=255, null=True, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='product',
            name='NFC',
            field=models.CharField(max_length=255, null=True, verbose_name='NFC'),
        ),
        migrations.AddField(
            model_name='product',
            name='Navigation_system',
            field=models.CharField(max_length=255, null=True, verbose_name='Системы навигации'),
        ),
        migrations.AddField(
            model_name='product',
            name='Network_support',
            field=models.CharField(max_length=255, null=True, verbose_name='Поддержка сетей'),
        ),
        migrations.AddField(
            model_name='product',
            name='OS',
            field=models.CharField(max_length=255, null=True, verbose_name='Операционная система'),
        ),
        migrations.AddField(
            model_name='product',
            name='OS_version',
            field=models.CharField(max_length=255, null=True, verbose_name='Версия операционной системы'),
        ),
        migrations.AddField(
            model_name='product',
            name='SIM_format',
            field=models.CharField(max_length=255, null=True, verbose_name='Формат SIM-карт'),
        ),
        migrations.AddField(
            model_name='product',
            name='Stereo_dynamics',
            field=models.CharField(max_length=255, null=True, verbose_name='Стереодинамики'),
        ),
        migrations.AddField(
            model_name='product',
            name='Thickness',
            field=models.CharField(max_length=255, null=True, verbose_name='Толщина'),
        ),
        migrations.AddField(
            model_name='product',
            name='Weight',
            field=models.CharField(max_length=255, null=True, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='product',
            name='Wi_Fi_standard',
            field=models.CharField(max_length=255, null=True, verbose_name='Стандарт Wi-Fi'),
        ),
        migrations.AddField(
            model_name='product',
            name='battery_charger',
            field=models.CharField(max_length=255, null=True, verbose_name='Зарядное устройство в комплекте'),
        ),
        migrations.AddField(
            model_name='product',
            name='battery_type',
            field=models.CharField(max_length=255, null=True, verbose_name='Тип аккумулятора'),
        ),
        migrations.AddField(
            model_name='product',
            name='biometric_protection',
            field=models.CharField(max_length=255, null=True, verbose_name='Биометрическая защита'),
        ),
        migrations.AddField(
            model_name='product',
            name='bluetooth_version',
            field=models.CharField(max_length=255, null=True, verbose_name='Версия Bluetooth'),
        ),
        migrations.AddField(
            model_name='product',
            name='connector_headphones',
            field=models.CharField(max_length=255, null=True, verbose_name='Разъем для наушников'),
        ),
        migrations.AddField(
            model_name='product',
            name='core_quantity',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество ядер'),
        ),
        migrations.AddField(
            model_name='product',
            name='density',
            field=models.CharField(max_length=255, null=True, verbose_name='Плотность пикселей'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_little',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='diagonal',
            field=models.CharField(max_length=255, null=True, verbose_name='Диагональ экрана (дюйм)'),
        ),
        migrations.AddField(
            model_name='product',
            name='equipment',
            field=models.CharField(max_length=255, null=True, verbose_name='Комплектация'),
        ),
        migrations.AddField(
            model_name='product',
            name='features_optional',
            field=models.CharField(max_length=255, null=True, verbose_name='Особенности, дополнительно'),
        ),
        migrations.AddField(
            model_name='product',
            name='format_audio_files',
            field=models.CharField(max_length=255, null=True, verbose_name='Форматы аудиофайлов'),
        ),
        migrations.AddField(
            model_name='product',
            name='interface',
            field=models.CharField(max_length=255, null=True, verbose_name='Интерфейс'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_camera_quantity',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество основных камер'),
        ),
        migrations.AddField(
            model_name='product',
            name='processor',
            field=models.CharField(max_length=255, null=True, verbose_name='Модель процессора'),
        ),
        migrations.AddField(
            model_name='product',
            name='processor_frequency',
            field=models.CharField(max_length=255, null=True, verbose_name='Частота процессора'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_SIM',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество физических SIM-карт'),
        ),
        migrations.AddField(
            model_name='product',
            name='release_year',
            field=models.CharField(max_length=255, null=True, verbose_name='Год релиза'),
        ),
        migrations.AddField(
            model_name='product',
            name='resolution',
            field=models.CharField(max_length=255, null=True, verbose_name='Разрешение экрана'),
        ),
        migrations.AddField(
            model_name='product',
            name='resolution_video',
            field=models.CharField(max_length=255, null=True, verbose_name='Разрешение видео и частота кадров'),
        ),
        migrations.AddField(
            model_name='product',
            name='tech_process',
            field=models.CharField(max_length=255, null=True, verbose_name='Техпроцесс'),
        ),
        migrations.AddField(
            model_name='product',
            name='technology',
            field=models.CharField(max_length=255, null=True, verbose_name='Технология изготовления экрана'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=255, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='product',
            name='video_format',
            field=models.CharField(max_length=255, null=True, verbose_name='Формат видеосъемки'),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(max_length=255, null=True, verbose_name='Гарантия'),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(max_length=255, null=True, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование'),
        ),
    ]
