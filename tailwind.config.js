// /** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      boxShadow: {
        "3xl": "0vw 0vw 0.5vw 0vw rgb(32 32 32 / 12%)",
        "4xl": " 0vw 0vw 0.5vw 0vw rgb(32 32 32 / 20%)",
        "5xl": " 0vw 0.5vw 0.5vw 0vw rgb(32 32 32 / 16%)",
      },
    },
  },    
  plugins: [
    require('flowbite/plugin')
]
}