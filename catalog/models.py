from django.db import models
from django.urls import reverse
from mptt import settings
from mptt.models import MPTTModel, TreeForeignKey



class Category(MPTTModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )

    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Каталог',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )


class Product(models.Model):
    # Основные
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to='catalog/',
        verbose_name='Изображение',
    )
    title = models.CharField(max_length=255, verbose_name='Наименование', null=True, )
    description_little = models.TextField(verbose_name='Краткое описание', null=True,)
    description = models.TextField(verbose_name='Описание', null=True,)
    price = models.TextField(verbose_name='Цена', null=True)
    # Заводские данные
    warranty = models.CharField(verbose_name='Гарантия', max_length=255, null=True,)
    # Общие параметры
    type = models.CharField(verbose_name='Тип', max_length=255, null=True,)
    Model = models.CharField(verbose_name='Модель', max_length=255, null=True,)
    release_year = models.CharField(verbose_name='Год релиза', max_length=255, null=True,)
    # Внешний вид
    Color = models.CharField(verbose_name='Цвет', max_length=255, null=True,)
    # Мобильная связь
    Network_support = models.CharField(verbose_name='Поддержка сетей', max_length=255, null=True,)
    SIM_format = models.CharField(verbose_name='Формат SIM-карт', max_length=255, null=True,)
    quantity_SIM = models.CharField(verbose_name='Количество физических SIM-карт', max_length=255, null=True,)
    # Экран
    diagonal = models.CharField(verbose_name='Диагональ экрана (дюйм)', max_length=255, null=True, )
    resolution = models.CharField(verbose_name='Разрешение экрана', max_length=255, null=True, )
    density = models.CharField(verbose_name='Плотность пикселей', max_length=255, null=True, )
    technology = models.CharField(verbose_name='Технология изготовления экрана', max_length=255, null=True, )
    Color_quantity = models.CharField(verbose_name='Количество цветов экрана', max_length=255, null=True, )
    # Корпус и защита
    Material = models.CharField(verbose_name='Материал корпуса', max_length=255, null=True, )
    # Система
    OS = models.CharField(verbose_name='Операционная система', max_length=255, null=True, )
    OS_version = models.CharField(verbose_name='Версия операционной системы', max_length=255, null=True, )
    processor = models.CharField(verbose_name='Модель процессора', max_length=255, null=True, )
    core_quantity = models.CharField(verbose_name='Количество ядер', max_length=255, null=True, )
    processor_frequency = models.CharField(verbose_name='Частота процессора', max_length=255, null=True, )
    tech_process = models.CharField(verbose_name='Техпроцесс', max_length=255, null=True, )
    GPU = models.CharField(verbose_name='Графический ускоритель', max_length=255, null=True, )
    Memory = models.CharField(verbose_name='Объем встроенной памяти', max_length=255, null=True, )
    Memory_card = models.CharField(verbose_name='Слот для карты памяти', max_length=255, null=True, )
    # Основная камера
    main_camera_quantity = models.CharField(verbose_name='Количество основных камер', max_length=255, null=True, )
    Megapixel_main_camera = models.CharField(verbose_name='Количество мегапикселей основной камеры', max_length=255,
                                             null=True, )
    # Видеосъемка
    video_format = models.CharField(verbose_name='Формат видеосъемки', max_length=255, null=True, )
    resolution_video = models.CharField(verbose_name='Разрешение видео и частота кадров', max_length=255, null=True, )
    # Фронтальная камера
    Megapixel_front_camera = models.CharField(verbose_name='Количество мегапикселей фронтальной камеры', max_length=255,
                                              null=True, )
    # Аудио
    Stereo_dynamics = models.CharField(verbose_name='Стереодинамики', max_length=255, null=True, )
    format_audio_files = models.CharField(verbose_name='Форматы аудиофайлов', max_length=255, null=True, )
    # Коммуникации
    bluetooth_version = models.CharField(verbose_name='Версия Bluetooth', max_length=255, null=True, )
    Wi_Fi_standard = models.CharField(verbose_name='Стандарт Wi-Fi', max_length=255, null=True, )
    NFC = models.CharField(verbose_name='NFC', max_length=255, null=True, )
    Navigation_system = models.CharField(verbose_name='Системы навигации', max_length=255, null=True, )
    Ik_port = models.CharField(verbose_name='ИК-порт', max_length=255, null=True, )
    # Проводные интерфейсы
    interface = models.CharField(verbose_name='Интерфейс', max_length=255, null=True, )
    connector_headphones = models.CharField(verbose_name='Разъем для наушников', max_length=255, null=True, )
    # Дополнительная информация
    Headphones_included = models.CharField(verbose_name='Наушники в комплекте', max_length=255, null=True, )
    battery_charger = models.CharField(verbose_name='Зарядное устройство в комплекте', max_length=255, null=True, )
    equipment = models.CharField(verbose_name='Комплектация', max_length=255, null=True, )
    biometric_protection = models.CharField(verbose_name='Биометрическая защита', max_length=255, null=True, )
    features_optional = models.CharField(verbose_name='Особенности, дополнительно', max_length=255, null=True, )
    # Питание
    battery_type = models.CharField(verbose_name='Тип аккумулятора', max_length=255, null=True, )
    # Габариты и вес
    width = models.CharField(verbose_name='Ширина', max_length=255, null=True, )
    Height = models.CharField(verbose_name='Высота', max_length=255, null=True, )
    Thickness = models.CharField(verbose_name='Толщина', max_length=255, null=True, )
    Weight = models.CharField(verbose_name='Вес', max_length=255, null=True, )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={
                'product_slug': self.slug,
                'category_slug': self.category.slug
            }
        )


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )
    review = models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
