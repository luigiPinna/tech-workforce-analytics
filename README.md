# Tech Workforce Analytics

A modern web application for visualizing and analyzing employee data across major tech companies. Built with React, Vite, and Tailwind CSS.

## Features

- 📊 Interactive dashboard showing key metrics
- 📈 Detailed company-specific analytics
- 🎨 Modern, responsive UI with Tailwind CSS
- 📱 Mobile-friendly design
- 🔄 Real-time data visualization
- 📊 Growth rate analysis
- 📈 Historical employee count trends

## Tech Stack

- **Frontend Framework**: React
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Charts**: Chart.js
- **Icons**: Heroicons

## Project Structure

```
tech-workforce-analytics/
├── frontend/                 # Frontend React application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── App.jsx         # Main application component
│   │   └── index.css       # Global styles
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
├── output/                  # Data files
│   └── employee_data.json  # Employee data
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tech-workforce-analytics.git
cd tech-workforce-analytics
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5174`

## Features in Detail

### Dashboard View
- Overview of all companies
- Total employee count across companies
- Average growth rate
- Interactive company cards
- Growth rate comparison chart

### Company Detail View
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