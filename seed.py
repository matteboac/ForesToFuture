"""
Deforestation Database Seed File
Integrates with existing Flask SQLAlchemy setup
Seeds yearly deforestation percentage data for 10 countries (2016-2025)
"""

from app import app
from models import db, DeforestationData, CountryMetadata

def seed_deforestation_data():
    """Seed the database with deforestation data"""
    
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

if __name__ == '__main__':
    seed_deforestation_data()