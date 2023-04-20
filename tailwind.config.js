/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './src/js/**/*.js',
      './forms/**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('daisyui')
  ],
}

