from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from catalog.models import Category, Product, Review


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30


admin.site.register(Category, CustomMPTTModelAdmin,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    list_filter = ('category',)
    fieldsets = (
        ('None', {'fields': ('title', 'description_little', 'description', 'image', 'price'),
                  }),
        ('Заводские данные', {'fields': ('warranty',)
                              }),
        ('Общие параметры', {'fields': (('type', 'Model'), 'release_year')
                             }),
        ('Внешний вид', {'fields': ('Color',)
                         }),
        ('Мобильная связь', {'fields': (('Network_support', 'SIM_format'), 'quantity_SIM')
                             }),
        ('Экран', {'fields': (('diagonal', 'resolution'), ('density', 'technology'), 'Color_quantity')
                   }),
        ('Корпус и защита', {'fields': ('Material',)
                             }),
        ('Система', {'fields': (('OS', 'OS_version'), ('processor', 'core_quantity'),
                                ('processor_frequency', 'tech_process'), ('GPU', 'Memory'), 'Memory_card')
                     }),
        ('Основная камера', {'fields': (('main_camera_quantity', 'Megapixel_main_camera'),)
                             }),
        ('Видеосъемка', {'fields': (('video_format', 'resolution_video'),)
                         }),
        ('Фронтальная камера', {'fields': ('Megapixel_front_camera',)
                                }),
        ('Аудио', {'fields': (('Stereo_dynamics', 'format_audio_files'),)
                   }),
        ('Коммуникации', {'fields': (('bluetooth_version', 'Wi_Fi_standard'), ('NFC', 'Navigation_system'), 'Ik_port')
                          }),
        ('Проводные интерфейсы', {'fields': (('interface', 'connector_headphones'),)
                                  }),
        ('Дополнительная информация', {'fields': (('Headphones_included', 'battery_charger'), ('equipment',
                                                  'biometric_protection'), 'features_optional')
                                       }),
        ('Питание', {'fields': ('battery_type',)
                     }),
        ('Габариты и вес', {'fields': (('width', 'Height'), ('Thickness', 'Weight'))
                            })
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating',)
