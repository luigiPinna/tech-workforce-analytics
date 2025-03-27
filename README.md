# Tech Workforce Analytics

A modern web application for visualizing and analyzing employee data across major tech companies. The project consists of a Python backend for data scraping and a React frontend for data visualization.

## Features

### Backend
- 🔍 Automated data scraping from company reports
- 📊 Data processing and normalization
- 💾 JSON data storage
- 🔄 Scheduled data updates
- 🛡️ Error handling and retry mechanisms

### Frontend
- 📊 Interactive dashboard showing key metrics
- 📈 Detailed company-specific analytics
- 🎨 Modern, responsive UI with Tailwind CSS
- 📱 Mobile-friendly design
- 🔄 Real-time data visualization
- 📊 Growth rate analysis
- 📈 Historical employee count trends

## Tech Stack

### Backend
- **Language**: Python 3.12
- **Web Scraping**: BeautifulSoup4, yfinance
- **Data Processing**: pandas, numpy
- **Data Storage**: JSON
- **Environment Management**: python-dotenv

### Frontend
- **Framework**: React
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Charts**: Chart.js
- **Icons**: Heroicons

## Project Structure

```
tech-workforce-analytics/
├── app/                     # Backend Python application
│   ├── config/             # Configuration files
│   ├── constants/          # Constants and configurations
│   └── main.py            # Main scraping script
├── frontend/               # Frontend React application
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.jsx       # Main application component
│   │   └── index.css     # Global styles
│   ├── public/           # Static assets
│   └── package.json      # Frontend dependencies
├── output/                # Data files
│   └── employee_data.json # Employee data
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.12
- Node.js (v18 or higher)
- npm (v9 or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tech-workforce-analytics.git
cd tech-workforce-analytics
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

4. Start the frontend development server:
```bash
npm run dev
```

5. Run the data scraping script:
```bash
python app/main.py
```

6. Open your browser and navigate to `http://localhost:5174`

## Features in Detail

### Backend Features
- Automated scraping of employee data from company reports
- Data normalization and processing
- Error handling and retry mechanisms
- Rate limiting to respect website policies
- Data validation and cleaning
- JSON data storage

### Frontend Features

#### Dashboard View
- Overview of all companies
- Total employee count across companies
- Average growth rate
- Interactive company cards
- Growth rate comparison chart

#### Company Detail View
- Historical employee count data
- Year-over-year growth rates
- Interactive line charts
- Key metrics and statistics

## Data Structure

The application uses a JSON data structure with the following format:

```json
{
  "TICKER": {
    "company": "company-name",
    "ticker": "TICKER",
    "data": [
      {
        "year": "YYYY",
        "employee_count": number
      }
    ]
  }
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data source: Company annual reports and public filings
- Icons: Heroicons
- Charts: Chart.js
- Web Scraping: BeautifulSoup4, yfinance