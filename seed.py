from app import app
from models import db, DeforestationData, CountryMetadata, Country, BiodiversityStatus

def seed_deforestation_data():
    
    # Deforestation percentage data (2016-2025)
    deforestation_data = [
        # Brazil - Largest net forest loss
        {'country': 'Brazil', 'year': 2016, 'percentage': 0.48, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2017, 'percentage': 0.49, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2018, 'percentage': 0.47, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2019, 'percentage': 0.52, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2020, 'percentage': 0.55, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2021, 'percentage': 0.53, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2022, 'percentage': 0.51, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2023, 'percentage': 0.47, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2024, 'percentage': 0.44, 'hectares': 294200},
        {'country': 'Brazil', 'year': 2025, 'percentage': 0.42, 'hectares': 294200},
        
        # Angola - 2nd highest
        {'country': 'Angola', 'year': 2016, 'percentage': 0.92, 'hectares': 51000},
        {'country': 'Angola', 'year': 2017, 'percentage': 0.95, 'hectares': 51000},
        {'country': 'Angola', 'year': 2018, 'percentage': 0.91, 'hectares': 51000},
        {'country': 'Angola', 'year': 2019, 'percentage': 0.88, 'hectares': 51000},
        {'country': 'Angola', 'year': 2020, 'percentage': 0.93, 'hectares': 51000},
        {'country': 'Angola', 'year': 2021, 'percentage': 0.90, 'hectares': 51000},
        {'country': 'Angola', 'year': 2022, 'percentage': 0.87, 'hectares': 51000},
        {'country': 'Angola', 'year': 2023, 'percentage': 0.85, 'hectares': 51000},
        {'country': 'Angola', 'year': 2024, 'percentage': 0.83, 'hectares': 51000},
        {'country': 'Angola', 'year': 2025, 'percentage': 0.80, 'hectares': 51000},
        
        # Tanzania
        {'country': 'Tanzania', 'year': 2016, 'percentage': 1.05, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2017, 'percentage': 1.08, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2018, 'percentage': 1.02, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2019, 'percentage': 0.98, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2020, 'percentage': 1.01, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2021, 'percentage': 0.97, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2022, 'percentage': 0.94, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2023, 'percentage': 0.91, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2024, 'percentage': 0.89, 'hectares': 46900},
        {'country': 'Tanzania', 'year': 2025, 'percentage': 0.86, 'hectares': 46900},
        
        # Myanmar
        {'country': 'Myanmar', 'year': 2016, 'percentage': 0.95, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2017, 'percentage': 0.98, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2018, 'percentage': 1.02, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2019, 'percentage': 0.93, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2020, 'percentage': 0.91, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2021, 'percentage': 0.89, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2022, 'percentage': 0.86, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2023, 'percentage': 0.84, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2024, 'percentage': 0.82, 'hectares': 29000},
        {'country': 'Myanmar', 'year': 2025, 'percentage': 0.80, 'hectares': 29000},
        
        # Democratic Republic of Congo
        {'country': 'DR Congo', 'year': 2016, 'percentage': 0.23, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2017, 'percentage': 0.24, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2018, 'percentage': 0.25, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2019, 'percentage': 0.26, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2020, 'percentage': 0.27, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2021, 'percentage': 0.28, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2022, 'percentage': 0.29, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2023, 'percentage': 0.30, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2024, 'percentage': 0.31, 'hectares': 28300},
        {'country': 'DR Congo', 'year': 2025, 'percentage': 0.32, 'hectares': 28300},
        
        # Mozambique
        {'country': 'Mozambique', 'year': 2016, 'percentage': 0.72, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2017, 'percentage': 0.74, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2018, 'percentage': 0.71, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2019, 'percentage': 0.69, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2020, 'percentage': 0.73, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2021, 'percentage': 0.70, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2022, 'percentage': 0.68, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2023, 'percentage': 0.66, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2024, 'percentage': 0.64, 'hectares': 26700},
        {'country': 'Mozambique', 'year': 2025, 'percentage': 0.62, 'hectares': 26700},
        
        # Cambodia - Highest annual percentage loss rate
        {'country': 'Cambodia', 'year': 2016, 'percentage': 3.45, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2017, 'percentage': 3.52, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2018, 'percentage': 3.38, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2019, 'percentage': 3.29, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2020, 'percentage': 3.41, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2021, 'percentage': 3.25, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2022, 'percentage': 3.15, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2023, 'percentage': 3.08, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2024, 'percentage': 3.01, 'hectares': 25100},
        {'country': 'Cambodia', 'year': 2025, 'percentage': 2.95, 'hectares': 25100},
        
        # Peru
        {'country': 'Peru', 'year': 2016, 'percentage': 0.33, 'hectares': 23900},
        {'country': 'Peru', 'year': 2017, 'percentage': 0.35, 'hectares': 23900},
        {'country': 'Peru', 'year': 2018, 'percentage': 0.36, 'hectares': 23900},
        {'country': 'Peru', 'year': 2019, 'percentage': 0.34, 'hectares': 23900},
        {'country': 'Peru', 'year': 2020, 'percentage': 0.32, 'hectares': 23900},
        {'country': 'Peru', 'year': 2021, 'percentage': 0.31, 'hectares': 23900},
        {'country': 'Peru', 'year': 2022, 'percentage': 0.30, 'hectares': 23900},
        {'country': 'Peru', 'year': 2023, 'percentage': 0.29, 'hectares': 23900},
        {'country': 'Peru', 'year': 2024, 'percentage': 0.28, 'hectares': 23900},
        {'country': 'Peru', 'year': 2025, 'percentage': 0.27, 'hectares': 23900},
        
        # Bolivia
        {'country': 'Bolivia', 'year': 2016, 'percentage': 0.48, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2017, 'percentage': 0.50, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2018, 'percentage': 0.52, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2019, 'percentage': 0.49, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2020, 'percentage': 0.47, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2021, 'percentage': 0.45, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2022, 'percentage': 0.43, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2023, 'percentage': 0.41, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2024, 'percentage': 0.39, 'hectares': 23200},
        {'country': 'Bolivia', 'year': 2025, 'percentage': 0.37, 'hectares': 23200},
        
        # Paraguay
        {'country': 'Paraguay', 'year': 2016, 'percentage': 1.25, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2017, 'percentage': 1.28, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2018, 'percentage': 1.22, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2019, 'percentage': 1.18, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2020, 'percentage': 1.21, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2021, 'percentage': 1.17, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2022, 'percentage': 1.14, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2023, 'percentage': 1.11, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2024, 'percentage': 1.08, 'hectares': 20700},
        {'country': 'Paraguay', 'year': 2025, 'percentage': 1.05, 'hectares': 20700},

        # Philippines - is consistently ranked among the top forest-loss hotspots in Southeast Asia
        {'country': 'Philippines', 'year': 2016, 'percentage': 0.70, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2017, 'percentage': 0.61, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2018, 'percentage': 0.38, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2019, 'percentage': 0.34, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2020, 'percentage': 0.34, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2021, 'percentage': 0.33, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2022, 'percentage': 0.33, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2023, 'percentage': 0.33, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2024, 'percentage': 0.24, 'hectares': 672800},
        {'country': 'Philippines', 'year': 2025, 'percentage': 0.24, 'hectares': 672800},

        # Indonesia
        {'country': 'Indonesia', 'year': 2016, 'percentage': 1.15, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2017, 'percentage': 1.12, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2018, 'percentage': 1.10, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2019, 'percentage': 1.08, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2020, 'percentage': 1.05, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2021, 'percentage': 1.03, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2022, 'percentage': 1.00, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2023, 'percentage': 0.98, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2024, 'percentage': 0.95, 'hectares': 68000},
        {'country': 'Indonesia', 'year': 2025, 'percentage': 0.92, 'hectares': 68000},

    # Malaysia
        {'country': 'Malaysia', 'year': 2016, 'percentage': 0.65, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2017, 'percentage': 0.63, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2018, 'percentage': 0.61, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2019, 'percentage': 0.60, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2020, 'percentage': 0.58, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2021, 'percentage': 0.56, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2022, 'percentage': 0.54, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2023, 'percentage': 0.53, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2024, 'percentage': 0.51, 'hectares': 34000},
        {'country': 'Malaysia', 'year': 2025, 'percentage': 0.50, 'hectares': 34000},

    # Thailand
        {'country': 'Thailand', 'year': 2016, 'percentage': 0.42, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2017, 'percentage': 0.40, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2018, 'percentage': 0.39, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2019, 'percentage': 0.37, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2020, 'percentage': 0.35, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2021, 'percentage': 0.33, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2022, 'percentage': 0.32, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2023, 'percentage': 0.30, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2024, 'percentage': 0.29, 'hectares': 28000},
        {'country': 'Thailand', 'year': 2025, 'percentage': 0.28, 'hectares': 28000},

    # Vietnam
        {'country': 'Vietnam', 'year': 2016, 'percentage': 0.55, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2017, 'percentage': 0.53, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2018, 'percentage': 0.50, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2019, 'percentage': 0.48, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2020, 'percentage': 0.46, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2021, 'percentage': 0.44, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2022, 'percentage': 0.42, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2023, 'percentage': 0.40, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2024, 'percentage': 0.38, 'hectares': 31000},
        {'country': 'Vietnam', 'year': 2025, 'percentage': 0.36, 'hectares': 31000},

    # India
        {'country': 'India', 'year': 2016, 'percentage': 0.31, 'hectares': 50000},
        {'country': 'India', 'year': 2017, 'percentage': 0.30, 'hectares': 50000},
        {'country': 'India', 'year': 2018, 'percentage': 0.29, 'hectares': 50000},
        {'country': 'India', 'year': 2019, 'percentage': 0.28, 'hectares': 50000},
        {'country': 'India', 'year': 2020, 'percentage': 0.27, 'hectares': 50000},
        {'country': 'India', 'year': 2021, 'percentage': 0.26, 'hectares': 50000},
        {'country': 'India', 'year': 2022, 'percentage': 0.25, 'hectares': 50000},
        {'country': 'India', 'year': 2023, 'percentage': 0.24, 'hectares': 50000},
        {'country': 'India', 'year': 2024, 'percentage': 0.23, 'hectares': 50000},
        {'country': 'India', 'year': 2025, 'percentage': 0.22, 'hectares': 50000},

    # China
        {'country': 'China', 'year': 2016, 'percentage': 0.15, 'hectares': 60000},
        {'country': 'China', 'year': 2017, 'percentage': 0.14, 'hectares': 60000},
        {'country': 'China', 'year': 2018, 'percentage': 0.13, 'hectares': 60000},
        {'country': 'China', 'year': 2019, 'percentage': 0.12, 'hectares': 60000},
        {'country': 'China', 'year': 2020, 'percentage': 0.11, 'hectares': 60000},
        {'country': 'China', 'year': 2021, 'percentage': 0.10, 'hectares': 60000},
        {'country': 'China', 'year': 2022, 'percentage': 0.10, 'hectares': 60000},
        {'country': 'China', 'year': 2023, 'percentage': 0.09, 'hectares': 60000},
        {'country': 'China', 'year': 2024, 'percentage': 0.08, 'hectares': 60000},
        {'country': 'China', 'year': 2025, 'percentage': 0.07, 'hectares': 60000},

    # Nigeria
        {'country': 'Nigeria', 'year': 2016, 'percentage': 0.95, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2017, 'percentage': 0.93, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2018, 'percentage': 0.91, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2019, 'percentage': 0.89, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2020, 'percentage': 0.87, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2021, 'percentage': 0.85, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2022, 'percentage': 0.83, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2023, 'percentage': 0.81, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2024, 'percentage': 0.79, 'hectares': 22000},
        {'country': 'Nigeria', 'year': 2025, 'percentage': 0.77, 'hectares': 22000},

    # Madagascar
        {'country': 'Madagascar', 'year': 2016, 'percentage': 1.80, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2017, 'percentage': 1.75, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2018, 'percentage': 1.70, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2019, 'percentage': 1.65, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2020, 'percentage': 1.60, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2021, 'percentage': 1.55, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2022, 'percentage': 1.50, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2023, 'percentage': 1.45, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2024, 'percentage': 1.40, 'hectares': 18000},
        {'country': 'Madagascar', 'year': 2025, 'percentage': 1.35, 'hectares': 18000},

    # Laos
        {'country': 'Laos', 'year': 2016, 'percentage': 1.05, 'hectares': 16000},
        {'country': 'Laos', 'year': 2017, 'percentage': 1.03, 'hectares': 16000},
        {'country': 'Laos', 'year': 2018, 'percentage': 1.01, 'hectares': 16000},
        {'country': 'Laos', 'year': 2019, 'percentage': 0.99, 'hectares': 16000},
        {'country': 'Laos', 'year': 2020, 'percentage': 0.97, 'hectares': 16000},
        {'country': 'Laos', 'year': 2021, 'percentage': 0.95, 'hectares': 16000},
        {'country': 'Laos', 'year': 2022, 'percentage': 0.93, 'hectares': 16000},
        {'country': 'Laos', 'year': 2023, 'percentage': 0.91, 'hectares': 16000},
        {'country': 'Laos', 'year': 2024, 'percentage': 0.89, 'hectares': 16000},
        {'country': 'Laos', 'year': 2025, 'percentage': 0.87, 'hectares': 16000},

    ]
    
    # Country metadata
    country_metadata = [

        {'country': 'Philippines', 'total_loss': 672800, 'avg_rate': 0.40, 'description': 'The Philippines experienced steady and continuous forest loss from 2016 to 2025, amounting to roughly 672,800 hectares during the 10-year period.'},
        {'country': 'Brazil', 'total_loss': 2942000, 'avg_rate': 0.49, 'description': 'By far the largest net forest loss over 2015-2025 (~2,942,000 hectares). Amazon deforestation driven by agriculture, cattle ranching, and illegal logging.'},
        {'country': 'Angola', 'total_loss': 510000, 'avg_rate': 0.89, 'description': '2nd highest net forest loss in that period (~510,000 ha). Deforestation driven by subsistence agriculture and charcoal production.'},
        {'country': 'Tanzania', 'total_loss': 469000, 'avg_rate': 0.97, 'description': 'Among top 3 countries with highest forest loss (~469,000 ha). Driven by agricultural expansion and firewood collection.'},
        {'country': 'Myanmar', 'total_loss': 290000, 'avg_rate': 0.89, 'description': 'Significant forest loss (~290,000 ha) due to agriculture expansion, rubber plantations, and mining.'},
        {'country': 'DR Congo', 'total_loss': 283000, 'avg_rate': 0.27, 'description': '~283,000 ha net forest loss. Among worst for recent tropical primary forest loss despite large forest reserves.'},
        {'country': 'Mozambique', 'total_loss': 267000, 'avg_rate': 0.69, 'description': 'Lost ~267,000 ha of forest. Significant deforestation from charcoal production and agricultural clearing.'},
        {'country': 'Cambodia', 'total_loss': 251000, 'avg_rate': 3.26, 'description': '~251,000 ha net forest loss. One of the highest annual percentage loss rates (~3.3% per year) driven by logging and plantations.'},
        {'country': 'Peru', 'total_loss': 239000, 'avg_rate': 0.31, 'description': '~239,000 ha net forest loss. Amazon deforestation from agriculture, mining, and illegal logging operations.'},
        {'country': 'Bolivia', 'total_loss': 232000, 'avg_rate': 0.45, 'description': '~232,000 ha forest loss. Among top for recent primary forest loss driven by agricultural expansion.'},
        {'country': 'Paraguay', 'total_loss': 207000, 'avg_rate': 1.17, 'description': '~207,000 ha forest loss. Chaco forest loss primarily for cattle ranching and soy production.'},
        {'country': 'Indonesia', 'total_loss': 680000, 'avg_rate': 1.04, 'description': '~680,000 ha forest loss. Deforestation driven by palm oil expansion, logging, and peatland fires.'},
        {'country': 'Malaysia', 'total_loss': 340000, 'avg_rate': 0.57, 'description': '~340,000 ha forest loss mainly from oil palm plantations and logging activities.'},
        {'country': 'Thailand', 'total_loss': 280000, 'avg_rate': 0.34, 'description': '~280,000 ha forest loss. Pressure from agriculture, urban expansion, and infrastructure development.'},
        {'country': 'Vietnam', 'total_loss': 310000, 'avg_rate': 0.45, 'description': '~310,000 ha forest loss largely due to commercial plantations and agricultural conversion.'},
        {'country': 'India', 'total_loss': 500000, 'avg_rate': 0.27, 'description': '~500,000 ha forest loss. Driven by development projects, mining, and agricultural expansion.'},
        {'country': 'China', 'total_loss': 600000, 'avg_rate': 0.11, 'description': '~600,000 ha forest loss. Despite reforestation efforts, losses occur from urbanization and infrastructure.'},
        {'country': 'Nigeria', 'total_loss': 220000, 'avg_rate': 0.87, 'description': '~220,000 ha forest loss. High pressure from fuelwood collection, agriculture, and population growth.'},
        {'country': 'Madagascar', 'total_loss': 180000, 'avg_rate': 1.58, 'description': '~180,000 ha forest loss. Slash-and-burn agriculture and charcoal production threaten biodiversity.'},
        {'country': 'Laos', 'total_loss': 160000, 'avg_rate': 0.96, 'description': '~160,000 ha forest loss. Hydropower projects, logging, and agricultural expansion are key drivers.'},

    ]

    with app.app_context():
        try:
            # Clear existing data
            DeforestationData.query.delete()
            CountryMetadata.query.delete()

            
            # Insert deforestation data
            for data in deforestation_data:
                entry = DeforestationData(
                    country=data['country'],
                    year=data['year'],
                    deforestation_percentage=data['percentage'],
                    forest_loss_hectares=data['hectares']
                )
                db.session.add(entry)
            
            # Insert country metadata
            for meta in country_metadata:
                entry = CountryMetadata(
                    country=meta['country'],
                    total_forest_loss_2015_2025=meta['total_loss'],
                    avg_annual_loss_rate=meta['avg_rate'],
                    description=meta['description']
                )
                db.session.add(entry)
            
            db.session.commit()
            print("✓ Database seeded successfully!")
            print(f"✓ Inserted {len(deforestation_data)} deforestation records")
            print(f"✓ Inserted {len(country_metadata)} country metadata records")
            
        except Exception as e:
            print(f"✗ Error seeding database: {e}")
            db.session.rollback()

def seed_countries():
    required_countries = ["Angola","Bolivia", "Brazil", "Cambodia", "DR Congo", "Mozambique", "Myanmar", "Paraguay", "Peru", "Philippines", "Tanzania","Indonesia", "Malaysia", "Thailand", "Vietnam", "India", "China", "Nigeria", "Madagascar", "Laos"]

    with app.app_context():
        for name in required_countries:
            if not Country.query.filter_by(name=name).first():
                db.session.add(Country(name=name))
        db.session.commit()
        print(f"✓ Countries ensured: {', '.join(required_countries)}")


def seed_biodiversity_data():
    biodiversity_data = [
    # Angola
    {'country_name': 'Angola', 'year': 2016, 'affected_species': 500, 'ecosystem_health_index': 60.0},
    {'country_name': 'Angola', 'year': 2017, 'affected_species': 520, 'ecosystem_health_index': 59.5},
    {'country_name': 'Angola', 'year': 2018, 'affected_species': 540, 'ecosystem_health_index': 59.0},
    {'country_name': 'Angola', 'year': 2019, 'affected_species': 560, 'ecosystem_health_index': 58.5},
    {'country_name': 'Angola', 'year': 2020, 'affected_species': 580, 'ecosystem_health_index': 58.0},
    {'country_name': 'Angola', 'year': 2021, 'affected_species': 600, 'ecosystem_health_index': 57.5},
    {'country_name': 'Angola', 'year': 2022, 'affected_species': 620, 'ecosystem_health_index': 57.0},
    {'country_name': 'Angola', 'year': 2023, 'affected_species': 640, 'ecosystem_health_index': 56.5},
    {'country_name': 'Angola', 'year': 2024, 'affected_species': 660, 'ecosystem_health_index': 56.0},
    {'country_name': 'Angola', 'year': 2025, 'affected_species': 680, 'ecosystem_health_index': 55.5},

    # Bolivia
    {'country_name': 'Bolivia', 'year': 2016, 'affected_species': 800, 'ecosystem_health_index': 65.0},
    {'country_name': 'Bolivia', 'year': 2017, 'affected_species': 830, 'ecosystem_health_index': 64.4},
    {'country_name': 'Bolivia', 'year': 2018, 'affected_species': 860, 'ecosystem_health_index': 63.8},
    {'country_name': 'Bolivia', 'year': 2019, 'affected_species': 890, 'ecosystem_health_index': 63.2},
    {'country_name': 'Bolivia', 'year': 2020, 'affected_species': 920, 'ecosystem_health_index': 62.6},
    {'country_name': 'Bolivia', 'year': 2021, 'affected_species': 950, 'ecosystem_health_index': 62.0},
    {'country_name': 'Bolivia', 'year': 2022, 'affected_species': 980, 'ecosystem_health_index': 61.4},
    {'country_name': 'Bolivia', 'year': 2023, 'affected_species': 1010, 'ecosystem_health_index': 60.8},
    {'country_name': 'Bolivia', 'year': 2024, 'affected_species': 1040, 'ecosystem_health_index': 60.2},
    {'country_name': 'Bolivia', 'year': 2025, 'affected_species': 1070, 'ecosystem_health_index': 59.6},

    # Brazil
    {'country_name': 'Brazil', 'year': 2016, 'affected_species': 1200, 'ecosystem_health_index': 58.0},
    {'country_name': 'Brazil', 'year': 2017, 'affected_species': 1250, 'ecosystem_health_index': 57.0},
    {'country_name': 'Brazil', 'year': 2018, 'affected_species': 1300, 'ecosystem_health_index': 57.0},
    {'country_name': 'Brazil', 'year': 2019, 'affected_species': 1350, 'ecosystem_health_index': 55.0},
    {'country_name': 'Brazil', 'year': 2020, 'affected_species': 1400, 'ecosystem_health_index': 54.0},
    {'country_name': 'Brazil', 'year': 2021, 'affected_species': 1450, 'ecosystem_health_index': 53.0},
    {'country_name': 'Brazil', 'year': 2022, 'affected_species': 1500, 'ecosystem_health_index': 52.0},
    {'country_name': 'Brazil', 'year': 2023, 'affected_species': 1550, 'ecosystem_health_index': 51.0},
    {'country_name': 'Brazil', 'year': 2024, 'affected_species': 1600, 'ecosystem_health_index': 50.0},
    {'country_name': 'Brazil', 'year': 2025, 'affected_species': 1650, 'ecosystem_health_index': 50.0},

    # Cambodia
    {'country_name': 'Cambodia', 'year': 2016, 'affected_species': 400, 'ecosystem_health_index': 55.0},
    {'country_name': 'Cambodia', 'year': 2017, 'affected_species': 415, 'ecosystem_health_index': 54.6},
    {'country_name': 'Cambodia', 'year': 2018, 'affected_species': 430, 'ecosystem_health_index': 54.2},
    {'country_name': 'Cambodia', 'year': 2019, 'affected_species': 445, 'ecosystem_health_index': 53.8},
    {'country_name': 'Cambodia', 'year': 2020, 'affected_species': 460, 'ecosystem_health_index': 53.4},
    {'country_name': 'Cambodia', 'year': 2021, 'affected_species': 475, 'ecosystem_health_index': 53.0},
    {'country_name': 'Cambodia', 'year': 2022, 'affected_species': 490, 'ecosystem_health_index': 52.6},
    {'country_name': 'Cambodia', 'year': 2023, 'affected_species': 505, 'ecosystem_health_index': 52.2},
    {'country_name': 'Cambodia', 'year': 2024, 'affected_species': 520, 'ecosystem_health_index': 51.8},
    {'country_name': 'Cambodia', 'year': 2025, 'affected_species': 535, 'ecosystem_health_index': 51.4},

    # DR Congo
    {'country_name': 'DR Congo', 'year': 2016, 'affected_species': 600, 'ecosystem_health_index': 60.0},
    {'country_name': 'DR Congo', 'year': 2017, 'affected_species': 650, 'ecosystem_health_index': 59.0},
    {'country_name': 'DR Congo', 'year': 2018, 'affected_species': 700, 'ecosystem_health_index': 59.0},
    {'country_name': 'DR Congo', 'year': 2019, 'affected_species': 750, 'ecosystem_health_index': 58.0},
    {'country_name': 'DR Congo', 'year': 2020, 'affected_species': 800, 'ecosystem_health_index': 57.0},
    {'country_name': 'DR Congo', 'year': 2021, 'affected_species': 850, 'ecosystem_health_index': 56.0},
    {'country_name': 'DR Congo', 'year': 2022, 'affected_species': 900, 'ecosystem_health_index': 55.0},
    {'country_name': 'DR Congo', 'year': 2023, 'affected_species': 950, 'ecosystem_health_index': 54.0},
    {'country_name': 'DR Congo', 'year': 2024, 'affected_species': 1000, 'ecosystem_health_index': 53.0},
    {'country_name': 'DR Congo', 'year': 2025, 'affected_species': 1082, 'ecosystem_health_index': 53.0},

    # Mozambique
    {'country_name': 'Mozambique', 'year': 2016, 'affected_species': 300, 'ecosystem_health_index': 57.0},
    {'country_name': 'Mozambique', 'year': 2017, 'affected_species': 312, 'ecosystem_health_index': 56.7},
    {'country_name': 'Mozambique', 'year': 2018, 'affected_species': 324, 'ecosystem_health_index': 56.4},
    {'country_name': 'Mozambique', 'year': 2019, 'affected_species': 336, 'ecosystem_health_index': 56.1},
    {'country_name': 'Mozambique', 'year': 2020, 'affected_species': 348, 'ecosystem_health_index': 55.8},
    {'country_name': 'Mozambique', 'year': 2021, 'affected_species': 360, 'ecosystem_health_index': 55.5},
    {'country_name': 'Mozambique', 'year': 2022, 'affected_species': 372, 'ecosystem_health_index': 55.2},
    {'country_name': 'Mozambique', 'year': 2023, 'affected_species': 384, 'ecosystem_health_index': 54.9},
    {'country_name': 'Mozambique', 'year': 2024, 'affected_species': 396, 'ecosystem_health_index': 54.6},
    {'country_name': 'Mozambique', 'year': 2025, 'affected_species': 408, 'ecosystem_health_index': 54.3},

    # Myanmar
    {'country_name': 'Myanmar', 'year': 2016, 'affected_species': 1000, 'ecosystem_health_index': 62.0},
    {'country_name': 'Myanmar', 'year': 2017, 'affected_species': 1025, 'ecosystem_health_index': 61.5},
    {'country_name': 'Myanmar', 'year': 2018, 'affected_species': 1050, 'ecosystem_health_index': 61.0},
    {'country_name': 'Myanmar', 'year': 2019, 'affected_species': 1075, 'ecosystem_health_index': 60.5},
    {'country_name': 'Myanmar', 'year': 2020, 'affected_species': 1100, 'ecosystem_health_index': 60.0},
    {'country_name': 'Myanmar', 'year': 2021, 'affected_species': 1125, 'ecosystem_health_index': 59.5},
    {'country_name': 'Myanmar', 'year': 2022, 'affected_species': 1150, 'ecosystem_health_index': 59.0},
    {'country_name': 'Myanmar', 'year': 2023, 'affected_species': 1175, 'ecosystem_health_index': 58.5},
    {'country_name': 'Myanmar', 'year': 2024, 'affected_species': 1200, 'ecosystem_health_index': 58.0},
    {'country_name': 'Myanmar', 'year': 2025, 'affected_species': 1225, 'ecosystem_health_index': 57.5},

    # Paraguay
    {'country_name': 'Paraguay', 'year': 2016, 'affected_species': 200, 'ecosystem_health_index': 58.0},
    {'country_name': 'Paraguay', 'year': 2017, 'affected_species': 210, 'ecosystem_health_index': 57.8},
    {'country_name': 'Paraguay', 'year': 2018, 'affected_species': 220, 'ecosystem_health_index': 57.6},
    {'country_name': 'Paraguay', 'year': 2019, 'affected_species': 230, 'ecosystem_health_index': 57.4},
    {'country_name': 'Paraguay', 'year': 2020, 'affected_species': 240, 'ecosystem_health_index': 57.2},
    {'country_name': 'Paraguay', 'year': 2021, 'affected_species': 250, 'ecosystem_health_index': 57.0},
    {'country_name': 'Paraguay', 'year': 2022, 'affected_species': 260, 'ecosystem_health_index': 56.8},
    {'country_name': 'Paraguay', 'year': 2023, 'affected_species': 270, 'ecosystem_health_index': 56.6},
    {'country_name': 'Paraguay', 'year': 2024, 'affected_species': 280, 'ecosystem_health_index': 56.4},
    {'country_name': 'Paraguay', 'year': 2025, 'affected_species': 290, 'ecosystem_health_index': 56.2},

    # Peru
    {'country_name': 'Peru', 'year': 2016, 'affected_species': 1500, 'ecosystem_health_index': 70.0},
    {'country_name': 'Peru', 'year': 2017, 'affected_species': 1540, 'ecosystem_health_index': 69.3},
    {'country_name': 'Peru', 'year': 2018, 'affected_species': 1580, 'ecosystem_health_index': 68.6},
    {'country_name': 'Peru', 'year': 2019, 'affected_species': 1620, 'ecosystem_health_index': 67.9},
    {'country_name': 'Peru', 'year': 2020, 'affected_species': 1660, 'ecosystem_health_index': 67.2},
    {'country_name': 'Peru', 'year': 2021, 'affected_species': 1700, 'ecosystem_health_index': 66.5},
    {'country_name': 'Peru', 'year': 2022, 'affected_species': 1740, 'ecosystem_health_index': 65.8},
    {'country_name': 'Peru', 'year': 2023, 'affected_species': 1780, 'ecosystem_health_index': 65.1},
    {'country_name': 'Peru', 'year': 2024, 'affected_species': 1820, 'ecosystem_health_index': 64.4},
    {'country_name': 'Peru', 'year': 2025, 'affected_species': 1860, 'ecosystem_health_index': 63.7},

    # Philippines
    {'country_name': 'Philippines', 'year': 2016, 'affected_species': 738, 'ecosystem_health_index': 0.0},
    {'country_name': 'Philippines', 'year': 2017, 'affected_species': 1196, 'ecosystem_health_index': 0.0},
    {'country_name': 'Philippines', 'year': 2018, 'affected_species': 1196, 'ecosystem_health_index': 41.4},
    {'country_name': 'Philippines', 'year': 2019, 'affected_species': 1196, 'ecosystem_health_index': 41.4},
    {'country_name': 'Philippines', 'year': 2020, 'affected_species': 1196, 'ecosystem_health_index': 41.4},
    {'country_name': 'Philippines', 'year': 2021, 'affected_species': 1196, 'ecosystem_health_index': 71.0},
    {'country_name': 'Philippines', 'year': 2022, 'affected_species': 1196, 'ecosystem_health_index': 38.6},
    {'country_name': 'Philippines', 'year': 2023, 'affected_species': 2000, 'ecosystem_health_index': 38.6},
    {'country_name': 'Philippines', 'year': 2024, 'affected_species': 2000, 'ecosystem_health_index': 33.9},
    {'country_name': 'Philippines', 'year': 2025, 'affected_species': 2000, 'ecosystem_health_index': 33.5},

    # Tanzania
    {'country_name': 'Tanzania', 'year': 2016, 'affected_species': 600, 'ecosystem_health_index': 59.0},
    {'country_name': 'Tanzania', 'year': 2017, 'affected_species': 618, 'ecosystem_health_index': 58.7},
    {'country_name': 'Tanzania', 'year': 2018, 'affected_species': 636, 'ecosystem_health_index': 58.4},
    {'country_name': 'Tanzania', 'year': 2019, 'affected_species': 654, 'ecosystem_health_index': 58.1},
    {'country_name': 'Tanzania', 'year': 2020, 'affected_species': 672, 'ecosystem_health_index': 57.8},
    {'country_name': 'Tanzania', 'year': 2021, 'affected_species': 690, 'ecosystem_health_index': 57.5},
    {'country_name': 'Tanzania', 'year': 2022, 'affected_species': 708, 'ecosystem_health_index': 57.2},
    {'country_name': 'Tanzania', 'year': 2023, 'affected_species': 726, 'ecosystem_health_index': 56.9},
    {'country_name': 'Tanzania', 'year': 2024, 'affected_species': 744, 'ecosystem_health_index': 56.6},
    {'country_name': 'Tanzania', 'year': 2025, 'affected_species': 762, 'ecosystem_health_index': 56.3},

   # Indonesia
    {'country_name': 'Indonesia', 'year': 2016, 'affected_species': 1100, 'ecosystem_health_index': 61.0},
    {'country_name': 'Indonesia', 'year': 2017, 'affected_species': 1130, 'ecosystem_health_index': 60.5},
    {'country_name': 'Indonesia', 'year': 2018, 'affected_species': 1160, 'ecosystem_health_index': 60.0},
    {'country_name': 'Indonesia', 'year': 2019, 'affected_species': 1190, 'ecosystem_health_index': 59.5},
    {'country_name': 'Indonesia', 'year': 2020, 'affected_species': 1220, 'ecosystem_health_index': 59.0},
    {'country_name': 'Indonesia', 'year': 2021, 'affected_species': 1250, 'ecosystem_health_index': 58.5},
    {'country_name': 'Indonesia', 'year': 2022, 'affected_species': 1280, 'ecosystem_health_index': 58.0},
    {'country_name': 'Indonesia', 'year': 2023, 'affected_species': 1310, 'ecosystem_health_index': 57.5},
    {'country_name': 'Indonesia', 'year': 2024, 'affected_species': 1340, 'ecosystem_health_index': 57.0},
    {'country_name': 'Indonesia', 'year': 2025, 'affected_species': 1370, 'ecosystem_health_index': 56.5},

# Malaysia
    {'country_name': 'Malaysia', 'year': 2016, 'affected_species': 450, 'ecosystem_health_index': 63.0},
    {'country_name': 'Malaysia', 'year': 2017, 'affected_species': 465, 'ecosystem_health_index': 62.6},
    {'country_name': 'Malaysia', 'year': 2018, 'affected_species': 480, 'ecosystem_health_index': 62.2},
    {'country_name': 'Malaysia', 'year': 2019, 'affected_species': 495, 'ecosystem_health_index': 61.8},
    {'country_name': 'Malaysia', 'year': 2020, 'affected_species': 510, 'ecosystem_health_index': 61.4},
    {'country_name': 'Malaysia', 'year': 2021, 'affected_species': 525, 'ecosystem_health_index': 61.0},
    {'country_name': 'Malaysia', 'year': 2022, 'affected_species': 540, 'ecosystem_health_index': 60.6},
    {'country_name': 'Malaysia', 'year': 2023, 'affected_species': 555, 'ecosystem_health_index': 60.2},
    {'country_name': 'Malaysia', 'year': 2024, 'affected_species': 570, 'ecosystem_health_index': 59.8},
    {'country_name': 'Malaysia', 'year': 2025, 'affected_species': 585, 'ecosystem_health_index': 59.4},

# Thailand
    {'country_name': 'Thailand', 'year': 2016, 'affected_species': 520, 'ecosystem_health_index': 64.0},
    {'country_name': 'Thailand', 'year': 2017, 'affected_species': 535, 'ecosystem_health_index': 63.6},
    {'country_name': 'Thailand', 'year': 2018, 'affected_species': 550, 'ecosystem_health_index': 63.2},
    {'country_name': 'Thailand', 'year': 2019, 'affected_species': 565, 'ecosystem_health_index': 62.8},
    {'country_name': 'Thailand', 'year': 2020, 'affected_species': 580, 'ecosystem_health_index': 62.4},
    {'country_name': 'Thailand', 'year': 2021, 'affected_species': 595, 'ecosystem_health_index': 62.0},
    {'country_name': 'Thailand', 'year': 2022, 'affected_species': 610, 'ecosystem_health_index': 61.6},
    {'country_name': 'Thailand', 'year': 2023, 'affected_species': 625, 'ecosystem_health_index': 61.2},
    {'country_name': 'Thailand', 'year': 2024, 'affected_species': 640, 'ecosystem_health_index': 60.8},
    {'country_name': 'Thailand', 'year': 2025, 'affected_species': 655, 'ecosystem_health_index': 60.4},

# Vietnam
    {'country_name': 'Vietnam', 'year': 2016, 'affected_species': 700, 'ecosystem_health_index': 62.0},
    {'country_name': 'Vietnam', 'year': 2017, 'affected_species': 725, 'ecosystem_health_index': 61.6},
    {'country_name': 'Vietnam', 'year': 2018, 'affected_species': 750, 'ecosystem_health_index': 61.2},
    {'country_name': 'Vietnam', 'year': 2019, 'affected_species': 775, 'ecosystem_health_index': 60.8},
    {'country_name': 'Vietnam', 'year': 2020, 'affected_species': 800, 'ecosystem_health_index': 60.4},
    {'country_name': 'Vietnam', 'year': 2021, 'affected_species': 825, 'ecosystem_health_index': 60.0},
    {'country_name': 'Vietnam', 'year': 2022, 'affected_species': 850, 'ecosystem_health_index': 59.6},
    {'country_name': 'Vietnam', 'year': 2023, 'affected_species': 875, 'ecosystem_health_index': 59.2},
    {'country_name': 'Vietnam', 'year': 2024, 'affected_species': 900, 'ecosystem_health_index': 58.8},
    {'country_name': 'Vietnam', 'year': 2025, 'affected_species': 925, 'ecosystem_health_index': 58.4},

# India
    {'country_name': 'India', 'year': 2016, 'affected_species': 820, 'ecosystem_health_index': 62.0},
    {'country_name': 'India', 'year': 2017, 'affected_species': 845, 'ecosystem_health_index': 61.6},
    {'country_name': 'India', 'year': 2018, 'affected_species': 870, 'ecosystem_health_index': 61.2},
    {'country_name': 'India', 'year': 2019, 'affected_species': 895, 'ecosystem_health_index': 60.8},
    {'country_name': 'India', 'year': 2020, 'affected_species': 920, 'ecosystem_health_index': 60.4},
    {'country_name': 'India', 'year': 2021, 'affected_species': 945, 'ecosystem_health_index': 60.0},
    {'country_name': 'India', 'year': 2022, 'affected_species': 970, 'ecosystem_health_index': 59.6},
    {'country_name': 'India', 'year': 2023, 'affected_species': 995, 'ecosystem_health_index': 59.2},
    {'country_name': 'India', 'year': 2024, 'affected_species': 1020, 'ecosystem_health_index': 58.8},
    {'country_name': 'India', 'year': 2025, 'affected_species': 1045, 'ecosystem_health_index': 58.4},

# China
    {'country_name': 'China', 'year': 2016, 'affected_species': 680, 'ecosystem_health_index': 64.0},
    {'country_name': 'China', 'year': 2017, 'affected_species': 700, 'ecosystem_health_index': 63.6},
    {'country_name': 'China', 'year': 2018, 'affected_species': 720, 'ecosystem_health_index': 63.2},
    {'country_name': 'China', 'year': 2019, 'affected_species': 740, 'ecosystem_health_index': 62.8},
    {'country_name': 'China', 'year': 2020, 'affected_species': 760, 'ecosystem_health_index': 62.4},
    {'country_name': 'China', 'year': 2021, 'affected_species': 780, 'ecosystem_health_index': 62.0},
    {'country_name': 'China', 'year': 2022, 'affected_species': 800, 'ecosystem_health_index': 61.6},
    {'country_name': 'China', 'year': 2023, 'affected_species': 820, 'ecosystem_health_index': 61.2},
    {'country_name': 'China', 'year': 2024, 'affected_species': 840, 'ecosystem_health_index': 60.8},
    {'country_name': 'China', 'year': 2025, 'affected_species': 860, 'ecosystem_health_index': 60.4},

# Nigeria
    {'country_name': 'Nigeria', 'year': 2016, 'affected_species': 750, 'ecosystem_health_index': 58.0},
    {'country_name': 'Nigeria', 'year': 2017, 'affected_species': 775, 'ecosystem_health_index': 57.6},
    {'country_name': 'Nigeria', 'year': 2018, 'affected_species': 800, 'ecosystem_health_index': 57.2},
    {'country_name': 'Nigeria', 'year': 2019, 'affected_species': 825, 'ecosystem_health_index': 56.8},
    {'country_name': 'Nigeria', 'year': 2020, 'affected_species': 850, 'ecosystem_health_index': 56.4},
    {'country_name': 'Nigeria', 'year': 2021, 'affected_species': 875, 'ecosystem_health_index': 56.0},
    {'country_name': 'Nigeria', 'year': 2022, 'affected_species': 900, 'ecosystem_health_index': 55.6},
    {'country_name': 'Nigeria', 'year': 2023, 'affected_species': 925, 'ecosystem_health_index': 55.2},
    {'country_name': 'Nigeria', 'year': 2024, 'affected_species': 950, 'ecosystem_health_index': 54.8},
    {'country_name': 'Nigeria', 'year': 2025, 'affected_species': 975, 'ecosystem_health_index': 54.4},

# Madagascar
    {'country_name': 'Madagascar', 'year': 2016, 'affected_species': 620, 'ecosystem_health_index': 59.0},
    {'country_name': 'Madagascar', 'year': 2017, 'affected_species': 645, 'ecosystem_health_index': 58.6},
    {'country_name': 'Madagascar', 'year': 2018, 'affected_species': 670, 'ecosystem_health_index': 58.2},
    {'country_name': 'Madagascar', 'year': 2019, 'affected_species': 695, 'ecosystem_health_index': 57.8},
    {'country_name': 'Madagascar', 'year': 2020, 'affected_species': 720, 'ecosystem_health_index': 57.4},
    {'country_name': 'Madagascar', 'year': 2021, 'affected_species': 745, 'ecosystem_health_index': 57.0},
    {'country_name': 'Madagascar', 'year': 2022, 'affected_species': 770, 'ecosystem_health_index': 56.6},
    {'country_name': 'Madagascar', 'year': 2023, 'affected_species': 795, 'ecosystem_health_index': 56.2},
    {'country_name': 'Madagascar', 'year': 2024, 'affected_species': 820, 'ecosystem_health_index': 55.8},
    {'country_name': 'Madagascar', 'year': 2025, 'affected_species': 845, 'ecosystem_health_index': 55.4},

# Laos
    {'country_name': 'Laos', 'year': 2016, 'affected_species': 560, 'ecosystem_health_index': 60.0},
    {'country_name': 'Laos', 'year': 2017, 'affected_species': 580, 'ecosystem_health_index': 59.6},
    {'country_name': 'Laos', 'year': 2018, 'affected_species': 600, 'ecosystem_health_index': 59.2},
    {'country_name': 'Laos', 'year': 2019, 'affected_species': 620, 'ecosystem_health_index': 58.8},
    {'country_name': 'Laos', 'year': 2020, 'affected_species': 640, 'ecosystem_health_index': 58.4},
    {'country_name': 'Laos', 'year': 2021, 'affected_species': 660, 'ecosystem_health_index': 58.0},
    {'country_name': 'Laos', 'year': 2022, 'affected_species': 680, 'ecosystem_health_index': 57.6},
    {'country_name': 'Laos', 'year': 2023, 'affected_species': 700, 'ecosystem_health_index': 57.2},
    {'country_name': 'Laos', 'year': 2024, 'affected_species': 720, 'ecosystem_health_index': 56.8},
    {'country_name': 'Laos', 'year': 2025, 'affected_species': 740, 'ecosystem_health_index': 56.4},

]


    with app.app_context():
        BiodiversityStatus.query.delete()
        db.session.commit()

        total = 0
        for row in biodiversity_data:
            country = Country.query.filter_by(name=row['country_name']).first()
            if not country:
                continue

            entry = BiodiversityStatus(
                country_id=country.id,
                country_name=row['country_name'],
                year=row['year'],
                affected_species=row['affected_species'],
                ecosystem_health_index=row['ecosystem_health_index']
            )
            db.session.add(entry)
            total += 1

        db.session.commit()
        print(f"✓ Seeded {total} biodiversity records!")

if __name__ == '__main__':
    seed_deforestation_data()
    seed_countries()   
    seed_biodiversity_data()