/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')

module.exports = {
  daisyui: {
    themes: ['pastel',
      {
        mytheme: {
        
"primary": "#caebf2",
        
"secondary": "#a9a9a9",
        
"accent": "#ff3b3f",
        
"neutral": "#25262b",
        
"base-100": "#f8fafc",
        
"info": "#64748b",
        
"success": "#818cf8",
        
"warning": "#ff3b3f",
        
"error": "#ff8989",
        },
      },
    ],
  },
  content: [
    './templates/**/*.html'
  ],
  plugins: [require("daisyui")],
}

