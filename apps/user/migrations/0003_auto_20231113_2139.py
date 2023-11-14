# Importa los modelos y otros necesarios
from django.db import migrations
from apps.user.models import Country, CountryMultilanguage


def populate_countries(apps, schema_editor):
    # Lista de países con sus datos
    countries_data = [
        {'alpha_2_code': 'US', 'abbreviation_name': 'USA', 'dial_code': '+1'},
        {'alpha_2_code': 'CA', 'abbreviation_name': 'CAN', 'dial_code': '+1'},
        {'alpha_2_code': 'MX', 'abbreviation_name': 'MEX', 'dial_code': '+52'},
        {'alpha_2_code': 'GB', 'abbreviation_name': 'GBR', 'dial_code': '+44'},
        {'alpha_2_code': 'DE', 'abbreviation_name': 'DEU', 'dial_code': '+49'},
        {'alpha_2_code': 'FR', 'abbreviation_name': 'FRA', 'dial_code': '+33'},
        {'alpha_2_code': 'IT', 'abbreviation_name': 'ITA', 'dial_code': '+39'},
        {'alpha_2_code': 'ES', 'abbreviation_name': 'ESP', 'dial_code': '+34'},
        {'alpha_2_code': 'BR', 'abbreviation_name': 'BRA', 'dial_code': '+55'},
        {'alpha_2_code': 'AR', 'abbreviation_name': 'ARG', 'dial_code': '+54'},
        {'alpha_2_code': 'AU', 'abbreviation_name': 'AUS', 'dial_code': '+61'},
        {'alpha_2_code': 'CN', 'abbreviation_name': 'CHN', 'dial_code': '+86'},
        {'alpha_2_code': 'JP', 'abbreviation_name': 'JPN', 'dial_code': '+81'},
        {'alpha_2_code': 'IN', 'abbreviation_name': 'IND', 'dial_code': '+91'},
        {'alpha_2_code': 'RU', 'abbreviation_name': 'RUS', 'dial_code': '+7'},
        {'alpha_2_code': 'ZA', 'abbreviation_name': 'ZAF', 'dial_code': '+27'},
        {'alpha_2_code': 'NG', 'abbreviation_name': 'NGA', 'dial_code': '+234'},
        {'alpha_2_code': 'EG', 'abbreviation_name': 'EGY', 'dial_code': '+20'},
        {'alpha_2_code': 'SA', 'abbreviation_name': 'SAU', 'dial_code': '+966'},
        {'alpha_2_code': 'KR', 'abbreviation_name': 'KOR', 'dial_code': '+82'},
        {'alpha_2_code': 'ID', 'abbreviation_name': 'IDN', 'dial_code': '+62'},
        {'alpha_2_code': 'TR', 'abbreviation_name': 'TUR', 'dial_code': '+90'},
        {'alpha_2_code': 'TH', 'abbreviation_name': 'THA', 'dial_code': '+66'},
        {'alpha_2_code': 'CA', 'abbreviation_name': 'CAN', 'dial_code': '+1'},
        {'alpha_2_code': 'AU', 'abbreviation_name': 'AUS', 'dial_code': '+61'},
        {'alpha_2_code': 'BR', 'abbreviation_name': 'BRA', 'dial_code': '+55'},
        {'alpha_2_code': 'CL', 'abbreviation_name': 'CHL', 'dial_code': '+56'},
        {'alpha_2_code': 'CO', 'abbreviation_name': 'COL', 'dial_code': '+57'},
        {'alpha_2_code': 'PE', 'abbreviation_name': 'PER', 'dial_code': '+51'},
        {'alpha_2_code': 'VE', 'abbreviation_name': 'VEN', 'dial_code': '+58'},
        {'alpha_2_code': 'ZA', 'abbreviation_name': 'ZAF', 'dial_code': '+27'},
        {'alpha_2_code': 'NG', 'abbreviation_name': 'NGA', 'dial_code': '+234'},
        {'alpha_2_code': 'KE', 'abbreviation_name': 'KEN', 'dial_code': '+254'},
        {'alpha_2_code': 'MA', 'abbreviation_name': 'MAR', 'dial_code': '+212'},
        {'alpha_2_code': 'EG', 'abbreviation_name': 'EGY', 'dial_code': '+20'},
        {'alpha_2_code': 'SA', 'abbreviation_name': 'SAU', 'dial_code': '+966'},
        {'alpha_2_code': 'IR', 'abbreviation_name': 'IRN', 'dial_code': '+98'},
        {'alpha_2_code': 'IN', 'abbreviation_name': 'IND', 'dial_code': '+91'},
        {'alpha_2_code': 'PK', 'abbreviation_name': 'PAK', 'dial_code': '+92'},
        {'alpha_2_code': 'BD', 'abbreviation_name': 'BGD', 'dial_code': '+880'},
        {'alpha_2_code': 'TH', 'abbreviation_name': 'THA', 'dial_code': '+66'},
        {'alpha_2_code': 'VN', 'abbreviation_name': 'VNM', 'dial_code': '+84'},
        {'alpha_2_code': 'PH', 'abbreviation_name': 'PHL', 'dial_code': '+63'},
        {'alpha_2_code': 'MY', 'abbreviation_name': 'MYS', 'dial_code': '+60'},
        {'alpha_2_code': 'SG', 'abbreviation_name': 'SGP', 'dial_code': '+65'},
        {'alpha_2_code': 'ID', 'abbreviation_name': 'IDN', 'dial_code': '+62'},
    ]

    countries_names_data = [
        {'alpha_2_code': 'US', 'name': 'United States', 'multilanguage_id': 1},
        {'alpha_2_code': 'MX', 'name': 'Mexico', 'multilanguage_id': 1},
        {'alpha_2_code': 'GB', 'name': 'United Kingdom', 'multilanguage_id': 1},
        {'alpha_2_code': 'DE', 'name': 'Germany', 'multilanguage_id': 1},
        {'alpha_2_code': 'FR', 'name': 'France', 'multilanguage_id': 1},
        {'alpha_2_code': 'IT', 'name': 'Italy', 'multilanguage_id': 1},
        {'alpha_2_code': 'ES', 'name': 'Spain', 'multilanguage_id': 1},
        {'alpha_2_code': 'BR', 'name': 'Brazil', 'multilanguage_id': 1},
        {'alpha_2_code': 'AR', 'name': 'Argentina', 'multilanguage_id': 1},
        {'alpha_2_code': 'AU', 'name': 'Australia', 'multilanguage_id': 1},
        {'alpha_2_code': 'CN', 'name': 'China', 'multilanguage_id': 1},
        {'alpha_2_code': 'JP', 'name': 'Japan', 'multilanguage_id': 1},
        {'alpha_2_code': 'IN', 'name': 'India', 'multilanguage_id': 1},
        {'alpha_2_code': 'RU', 'name': 'Russia', 'multilanguage_id': 1},
        {'alpha_2_code': 'ZA', 'name': 'South Africa', 'multilanguage_id': 1},
        {'alpha_2_code': 'NG', 'name': 'Nigeria', 'multilanguage_id': 1},
        {'alpha_2_code': 'EG', 'name': 'Egypt', 'multilanguage_id': 1},
        {'alpha_2_code': 'SA', 'name': 'Saudi Arabia', 'multilanguage_id': 1},
        {'alpha_2_code': 'KR', 'name': 'South Korea', 'multilanguage_id': 1},
        {'alpha_2_code': 'ID', 'name': 'Indonesia', 'multilanguage_id': 1},
        {'alpha_2_code': 'TR', 'name': 'Turkey', 'multilanguage_id': 1},
        {'alpha_2_code': 'TH', 'name': 'Thailand', 'multilanguage_id': 1},
        {'alpha_2_code': 'CA', 'name': 'Canada', 'multilanguage_id': 1},
        {'alpha_2_code': 'AU', 'name': 'Australia', 'multilanguage_id': 1},
        {'alpha_2_code': 'BR', 'name': 'Brazil', 'multilanguage_id': 1},
        {'alpha_2_code': 'CL', 'name': 'Chile', 'multilanguage_id': 1},
        {'alpha_2_code': 'CO', 'name': 'Colombia', 'multilanguage_id': 1},
        {'alpha_2_code': 'PE', 'name': 'Peru', 'multilanguage_id': 1},
        {'alpha_2_code': 'VE', 'name': 'Venezuela', 'multilanguage_id': 1},
        {'alpha_2_code': 'ZA', 'name': 'South Africa', 'multilanguage_id': 1},
        {'alpha_2_code': 'NG', 'name': 'Nigeria', 'multilanguage_id': 1},
        {'alpha_2_code': 'KE', 'name': 'Kenya', 'multilanguage_id': 1},
        {'alpha_2_code': 'MA', 'name': 'Morocco', 'multilanguage_id': 1},
        {'alpha_2_code': 'EG', 'name': 'Egypt', 'multilanguage_id': 1},
        {'alpha_2_code': 'SA', 'name': 'Saudi Arabia', 'multilanguage_id': 1},
        {'alpha_2_code': 'IR', 'name': 'Iran', 'multilanguage_id': 1},
        {'alpha_2_code': 'IN', 'name': 'India', 'multilanguage_id': 1},
        {'alpha_2_code': 'PK', 'name': 'Pakistan', 'multilanguage_id': 1},
        {'alpha_2_code': 'BD', 'name': 'Bangladesh', 'multilanguage_id': 1},
        {'alpha_2_code': 'TH', 'name': 'Thailand', 'multilanguage_id': 1},
        {'alpha_2_code': 'VN', 'name': 'Vietnam', 'multilanguage_id': 1},
        {'alpha_2_code': 'PH', 'name': 'Philippines', 'multilanguage_id': 1},
        {'alpha_2_code': 'MY', 'name': 'Malaysia', 'multilanguage_id': 1},
        {'alpha_2_code': 'SG', 'name': 'Singapore', 'multilanguage_id': 1},
        {'alpha_2_code': 'ID', 'name': 'Indonesia', 'multilanguage_id': 1},
    ]

    # Usa el modelo Country para crear y guardar países
    Country.objects.bulk_create([
        Country(**data) for data in countries_data
    ])

    # Usa el modelo CountryMultilanguage para asociar nombres a los países
    try:
        for country_data in countries_names_data:

            country = Country.objects.get(
                alpha_2_code=country_data['alpha_2_code'])

            CountryMultilanguage.objects.create(
                # Puedes usar otro campo existente en lugar de 'abbreviation_name'
                name=country_data['name'],
                country=country,
                multilanguage_id=country_data['multilanguage_id']
            )

    except Exception as e:
        print('error: ', country_data)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_country_countrymultilanguage_alter_user_country_and_more'),

    ]

    operations = [
        migrations.RunPython(populate_countries),
    ]
