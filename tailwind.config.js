/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')

module.exports = {
  daisyui: {
    themes: ["dracula"],
  },
  content: [
    './templates/**/*.html'
  ],
  plugins: [require("daisyui")],
}

