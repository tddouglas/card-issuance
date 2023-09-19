/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js,ts,vue}", "./index.html"],
    darkMode: "class",
    theme: {
        colors: {
            green: "rgba(0,186,126,1)"
        },
        backgroundColor: ({theme}) => ({
            "adyen-dark": "rgba(0,17,44,1)",
            hover: "rgb(0,12,44)"
        }),
        textColor: ({theme}) => ({
            // light & dark combined into 1 in main.css
            "adyen-dark-text": "#fff",
            ...theme("colors")
        }),
        fontFamily: {
            body: [
                "fakt", "-apple-system", "blinkmacsystemfont", "Segoe UI", "roboto", "oxygen", "ubuntu", "cantarell", "Open Sans", "Helvetica Neue", "sans-serif"
            ],
            sans: ["Graphik", "sans-serif"],
            serif: ["Merriweather", "serif"]
        },
        extend: {
            boxShadow: {
                'tileShadow': 'inset 0 0 0 2px rgb(255 255 255 / 0.9), 0 4px 6px -4px rgb(255 255 255 / 0.9)',
            }
        }
    },
    plugins: []
}