/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    // Aggiungi questi se usi altre cartelle o file rilevanti
  ],
  theme: {
    extend: {
      // Esempi di personalizzazioni (opzionali)
      colors: {
        primary: 'hsl(210, 80%, 54%)',
        dark: {
          900: 'hsl(224, 28%, 12%)'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Consigliato per React
      },
    },
  },
  plugins: [
    // Aggiungi plugin utili (opzionali)
    require('@tailwindcss/typography'), // Per stili di testo avanzati
    // require('@tailwindcss/forms'), // Per stili di form predefiniti
  ],
  corePlugins: {
    // Ottimizzazione per React (opzionale)
    preflight: true, // Reset CSS di Tailwind (utile per React)
  }
}