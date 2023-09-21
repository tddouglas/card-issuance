/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js,ts,vue}", "./index.html"],
    darkMode: "class",
    theme: {
        colors: {
            green: "rgba(0,186,126,1)",
            "adyen-white": "#f7f8f9",
            "adyen-grey": "#dee1e6"
        },
        backgroundColor: ({theme}) => ({
            "adyen-dark": "rgba(0,17,44,1)",
            "adyen-light": "#f7f8f9",
            "adyen-grey": "#dee1e6",
            hover: "rgb(0,12,44)"
        }),
        textColor: ({theme}) => ({
            // light & dark combined into 1 in main.css
            "adyen-dark-text": "#fff",
            "adyen-light-text": "rgba(0,17,44,1)",
            ...theme("colors")
        }),
        fontFamily: {
            body: [
                "fakt", "-apple-system", "blinkmacsystemfont", "Segoe UI", "roboto", "oxygen", "ubuntu", "cantarell", "Open Sans", "Helvetica Neue", "sans-serif"
            ],
            dropdown: ["Fakt","Helvetica","Arial","sans-serif"]
        },
        extend: {
            boxShadow: {
                'tileShadow': 'inset 0 0 0 2px rgb(255 255 255 / 0.9), 0 4px 6px -4px rgb(255 255 255 / 0.9)',
            }
        }
    },
    plugins: []
}