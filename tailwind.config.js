/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily : {
        "Dorna" : "Dorna" ,
        "YekanBakh" : "YekanBakh",
        "Kalame" : "Kalame"
      }
      ,
      colors : {
        "primary" : "#AF47D2",
        "secondary" : "#021959"
      },
      screens : {
        "xs" : "368px",
        "sm" : "576px"
      }
    },
  },
  plugins: [],
}