/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './todo_py/blueprints/web/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'py-blue': '#306998',
        'py-yellow': '#FFD43B',
      },
    },
  },
  plugins: [],
  darkMode: 'class'
}
