from pathlib import Path
import streamlit as st

from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge
from st_on_hover_tabs import on_hover_tabs
from streamlit.components.v1 import html
from PIL import Image
st.set_page_config(layout="wide")


with open("assets/style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)
       
    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home','Analyse', 'Prédiction', 'Recommandations'], 
                            iconName=['home','manage_search','app_registration', 'settings_applications'], default_choice=0)


    if tabs =='Home':
        context_projet_html_string = f'''
                
                <body>
                <div class="header">
                <div class="mobile-plan-banner -container">
                    <div class="badging-indicator">Nouveau&nbsp;!</div>
                        <div id="" class="mobile-plan-banner -banner-offer-text" data-uia="">
                            <span>Offres désormais disponibles à partir de <span class="mobile-plan-banner -price-label">5,99&nbsp;€</span>.
                            </span>/mois</div>
                            <div class="mobile-plan-button-cta btn-small --alternate-cta-treatment"><a data-uia="ad_plan_banner" class="btn btn-outline btn-small" href="/signup" target="_top">En savoir plus<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="button-icon icon-chevron-next"><path fill-rule="evenodd" clip-rule="evenodd" d="M7.29297 19.2928L14.5859 12L7.29297 4.70706L8.70718 3.29285L16.7072 11.2928C16.8947 11.4804 17.0001 11.7347 17.0001 12C17.0001 12.2652 16.8947 12.5195 16.7072 12.7071L8.70718 20.7071L7.29297 19.2928Z" fill="currentColor"></path></svg></a></div>
                            </div>
                    <nav>
                        <img src="netfloox_logo.png" class="logo">
                        <div class="default-ltr-cache-dk343m ea3diy33">
                            <div role="img" aria-hidden="true" class="default-ltr-cache-iyxs8w e19utwz74">
                                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="Hawkins-Icon Hawkins-Icon-Small"><path fill-rule="evenodd" clip-rule="evenodd" d="M8,14.5c0.23033,0 0.84266,-0.2257 1.48679,-1.514c0.27614,-0.5523 0.51294,-1.2239 0.68801,-1.986h-4.3496c0.17507,0.7621 0.41187,1.4337 0.68801,1.986c0.64413,1.2883 1.25646,1.514 1.48679,1.514zM10.4224,9.5c0.0504,-0.47923 0.0776,-0.98089 0.0776,-1.5c0,-0.51911 -0.0272,-1.02077 -0.0776,-1.5h-4.84478c-0.05046,0.47923 -0.07762,0.98089 -0.07762,1.5c0,0.51911 0.02716,1.02077 0.07762,1.5zM11.7092,11c-0.227,1.1217 -0.5775,2.117 -1.0178,2.9184c1.3223,-0.6023 2.4073,-1.6347 3.0764,-2.9184zM14.5,8c0,-0.51627 -0.0602,-1.01848 -0.1739,-1.5h-2.3963c0.0461,0.48588 0.0702,0.98731 0.0702,1.5c0,0.51269 -0.0241,1.01412 -0.0702,1.5h2.3963c0.1137,-0.48152 0.1739,-0.98373 0.1739,-1.5zM4,8c0,-0.51269 0.02411,-1.01412 0.0702,-1.5h-2.39627c-0.11374,0.48152 -0.17393,0.98373 -0.17393,1.5c0,0.51627 0.06019,1.01848 0.17393,1.5h2.39627c-0.04609,-0.48588 -0.0702,-0.98731 -0.0702,-1.5zM5.30864,13.9184c-0.44032,-0.8014 -0.79085,-1.7967 -1.01788,-2.9184h-2.05855c0.66907,1.2837 1.75414,2.3161 3.07643,2.9184zM5.8252,5h4.3496c-0.17507,-0.76207 -0.41187,-1.43374 -0.68801,-1.98603c-0.64413,-1.28826 -1.25646,-1.51397 -1.48679,-1.51397c-0.23033,0 -0.84266,0.22571 -1.48679,1.51397c-0.27614,0.55229 -0.51294,1.22396 -0.68801,1.98603zM11.7092,5h2.0586c-0.6691,-1.28373 -1.7541,-2.31611 -3.0764,-2.91838c0.4403,0.8014 0.7908,1.79668 1.0178,2.91838zM2.23221,5h2.05855c0.22703,-1.1217 0.57756,-2.11698 1.01788,-2.91838c-1.32229,0.60227 -2.40736,1.63466 -3.07643,2.91838zM8,0c4.4183,0 8,3.58172 8,8c0,4.4183 -3.5817,8 -8,8c-4.41828,0 -8,-3.5817 -8,-8c0,-4.41828 3.58172,-8 8,-8z" fill="currentColor"></path>
                                </svg>
                            </div>
                            <select id="27f4999ebd299" name="LanguageSelect" data-uia="language-picker-header" aria-describedby="4a85d36b6ff5d">
                                <option selected="" lang="fr" label="Français" value="fr-FR">Français</option>
                                <option lang="en" label="English" value="en-FR">English</option></select>
                                <div aria-hidden="true" class="default-ltr-cache-9oi2oi ea3diy32">
                                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="Hawkins-Icon Hawkins-Icon-Small" aria-hidden="true">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M12.5225,5.99902c0.1576,0 0.2272,0.19843 0.1041,0.29687l-4.41973,3.53579c-0.12176,0.09741 -0.29477,0.09741 -0.41653,0l-4.41975,-3.53579c-0.12304,-0.09844 -0.05344,-0.29687 0.10414,-0.29687z" fill="currentColor"></path>
                                    </svg>
                                </div>
                        </div>
                    </nav>
                    </div>
               
                
                
                </body>
                </html>
                    
                
                '''
        st.markdown(context_projet_html_string, unsafe_allow_html=True)
        badge(type="github", name="data-IA-2022/NETFLOOX_manuel_adrien_tarik")

    elif tabs == 'Analyse':
        st.title("Analyse des données de la base")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Prédiction':
        st.title("Prédiction de la popularité du film soumis")
        st.write('Name of option is {}'.format(tabs))
    
    elif tabs == 'Recommandations':
        st.title("Recommandations de film selon vos préférences")
        st.write('Name of option is {}'.format(tabs))

    
    
    

    
        
# <svg width="721" height="168" viewBox="0 0 721 168" fill="none" xmlns="http://www.w3.org/2000/svg">
# <path d="M59.9728 2.98555H83.5451V158.411L56.2403 161.274L24.7902 48.0486L24.0782 48.1405V164.351C16.1199 165.327 8.42173 166.271 0.446991 167.247V2.74055C10.8014 2.74055 21.0577 2.58655 31.2944 2.93855C32.5575 2.98155 34.3675 5.55357 34.8339 7.23857C41.655 31.7956 48.281 56.4036 54.9751 80.9946C56.3063 85.8846 57.7293 90.7506 59.9728 95.4616V2.98555Z" fill="#E00808"/>
# <path d="M540.37 88.2286C540.509 68.7366 540.021 49.7156 540.978 30.7626C541.788 14.7126 552.998 3.39755 569.439 1.32255C577.317 0.329553 585.643 0.465544 593.468 1.76954C608.335 4.24654 618.5 15.5876 620.395 30.2416C620.949 34.5276 621.251 38.8716 621.269 43.1916C621.378 68.3566 621.495 93.5236 621.301 118.689C621.259 124.122 620.661 129.747 619.088 134.933C615.979 145.183 609.043 152.563 597.962 154.725C581.234 157.987 565.446 155.755 552.011 144.592C544.994 138.762 541.466 130.962 540.994 122.208C540.392 111.068 540.544 99.8896 540.37 88.2276M594.627 96.7286C594.575 77.8996 594.558 59.0716 594.431 40.2426C594.41 37.2636 594.148 34.2386 593.549 31.3206C592.452 25.9776 588.373 22.6865 582.767 22.1835C572.216 21.2345 566.913 25.9996 566.901 36.8756C566.876 63.5356 566.991 90.1956 567.084 116.856C567.09 118.681 567.28 120.519 567.554 122.326C568.813 130.668 574.626 134.823 584.116 134.228C590.676 133.816 594.493 129.241 594.627 121.222C594.758 113.393 594.64 105.56 594.627 96.7286Z" fill="#E00909"/>
# <path d="M443.565 108.968C443.508 85.1656 443.406 61.8376 443.435 38.5086C443.441 34.5276 443.518 30.4435 444.393 26.5845C447.254 13.9715 455.174 5.64757 468.094 2.13957C477.883 -0.517434 487.912 -0.730444 497.683 1.67256C514.724 5.86456 523.686 16.3496 524.088 34.1786C524.725 62.4926 524.791 90.8366 524.213 119.151C523.846 137.083 511.75 148.66 493.198 149.413C484.754 149.756 475.846 149.103 467.799 146.78C453.515 142.658 442.754 131.688 443.565 108.968ZM495.283 26.1876C492.269 24.5256 489.415 21.8646 486.212 21.3846C475.493 19.7806 469.994 24.8906 469.964 35.9346C469.894 61.5506 469.95 87.1676 469.985 112.785C469.987 114.44 470.121 116.115 470.401 117.746C471.757 125.649 477.196 129.599 485.79 129.004C493.864 128.445 497.392 124.756 497.829 116.395C497.881 115.399 497.904 114.4 497.901 113.403C497.82 87.7856 497.804 62.1686 497.563 36.5526C497.533 33.3226 496.322 30.1036 495.283 26.1876Z" fill="#E00808"/>
# <path d="M686.849 23.5415C689.098 17.3785 691.034 11.5166 693.368 5.80656C693.898 4.51356 695.78 2.93655 697.098 2.88355C704.289 2.59755 711.498 2.74757 719.463 2.74757C716.496 10.8056 713.844 18.0865 711.137 25.3485C704.791 42.3785 698.265 59.3506 692.199 76.4746C691.138 79.4706 691.036 83.4016 692.074 86.3836C701.386 113.128 711.052 139.756 720.89 167.192C711.592 166.126 702.837 165.244 694.145 163.962C693.125 163.812 692.155 161.554 691.663 160.112C686.109 143.868 680.655 127.591 675.168 111.325C674.704 109.948 674.193 108.586 673.283 106.04L653.271 159.96L628.292 157.497C630.335 152.162 632.169 147.257 634.091 142.383C641.799 122.831 649.627 103.323 657.139 83.6986C658.041 81.3396 658.06 78.1146 657.18 75.7476C648.691 52.9336 639.919 30.2176 631.241 7.47056C630.663 5.95456 630.191 4.40056 629.598 2.65656C638.432 2.65656 646.824 2.51655 655.201 2.81455C656.389 2.85755 658.052 4.83655 658.556 6.23655C663.812 20.8245 668.874 35.4795 673.998 50.1115C674.437 51.3625 674.945 52.5906 675.714 54.5916C679.532 43.9016 683.106 33.8995 686.849 23.5415ZM103.409 127.229V2.66355H175.946V23.6736H130.588V63.7906H166.37V84.7185L130.471 86.2846V132.881L175.509 130.027V151.262L103.408 156.727V127.229H103.409Z" fill="#E00909"/>
# <path d="M279.618 2.51057H349.727V22.5356H306.704V62.1405H340.385V82.9016H306.173V145.452H279.618V2.51057Z" fill="#E00808"/>
# <path d="M238.666 147.718L212.348 148.977V23.3716H184.922V2.50856H266.468V22.9296H238.668C238.668 59.5415 238.668 95.6326 238.666 132.224V147.718Z" fill="#E00A0A"/>
# <path d="M430.54 145.669C407.947 145.657 385.805 145.657 363.341 145.657V2.43855H389.574V124.639H433.619C433.619 131.63 433.683 137.889 433.505 144.139C433.489 144.675 431.866 145.168 430.54 145.669Z" fill="#E00707"/>
# </svg>


# <svg viewBox="0 0 111 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="default-ltr-cache-ag96qb">
# <g><path d="M59.9728 2.98555H83.5451V158.411L56.2403 161.274L24.7902 48.0486L24.0782 48.1405V164.351C16.1199 165.327 8.42173 166.271 0.446991 167.247V2.74055C10.8014 2.74055 21.0577 2.58655 31.2944 2.93855C32.5575 2.98155 34.3675 5.55357 34.8339 7.23857C41.655 31.7956 48.281 56.4036 54.9751 80.9946C56.3063 85.8846 57.7293 90.7506 59.9728 95.4616V2.98555Z" fill="#E00808"/>
# <path d="M540.37 88.2286C540.509 68.7366 540.021 49.7156 540.978 30.7626C541.788 14.7126 552.998 3.39755 569.439 1.32255C577.317 0.329553 585.643 0.465544 593.468 1.76954C608.335 4.24654 618.5 15.5876 620.395 30.2416C620.949 34.5276 621.251 38.8716 621.269 43.1916C621.378 68.3566 621.495 93.5236 621.301 118.689C621.259 124.122 620.661 129.747 619.088 134.933C615.979 145.183 609.043 152.563 597.962 154.725C581.234 157.987 565.446 155.755 552.011 144.592C544.994 138.762 541.466 130.962 540.994 122.208C540.392 111.068 540.544 99.8896 540.37 88.2276M594.627 96.7286C594.575 77.8996 594.558 59.0716 594.431 40.2426C594.41 37.2636 594.148 34.2386 593.549 31.3206C592.452 25.9776 588.373 22.6865 582.767 22.1835C572.216 21.2345 566.913 25.9996 566.901 36.8756C566.876 63.5356 566.991 90.1956 567.084 116.856C567.09 118.681 567.28 120.519 567.554 122.326C568.813 130.668 574.626 134.823 584.116 134.228C590.676 133.816 594.493 129.241 594.627 121.222C594.758 113.393 594.64 105.56 594.627 96.7286Z" fill="#E00909"/>
# <path d="M443.565 108.968C443.508 85.1656 443.406 61.8376 443.435 38.5086C443.441 34.5276 443.518 30.4435 444.393 26.5845C447.254 13.9715 455.174 5.64757 468.094 2.13957C477.883 -0.517434 487.912 -0.730444 497.683 1.67256C514.724 5.86456 523.686 16.3496 524.088 34.1786C524.725 62.4926 524.791 90.8366 524.213 119.151C523.846 137.083 511.75 148.66 493.198 149.413C484.754 149.756 475.846 149.103 467.799 146.78C453.515 142.658 442.754 131.688 443.565 108.968ZM495.283 26.1876C492.269 24.5256 489.415 21.8646 486.212 21.3846C475.493 19.7806 469.994 24.8906 469.964 35.9346C469.894 61.5506 469.95 87.1676 469.985 112.785C469.987 114.44 470.121 116.115 470.401 117.746C471.757 125.649 477.196 129.599 485.79 129.004C493.864 128.445 497.392 124.756 497.829 116.395C497.881 115.399 497.904 114.4 497.901 113.403C497.82 87.7856 497.804 62.1686 497.563 36.5526C497.533 33.3226 496.322 30.1036 495.283 26.1876Z" fill="#E00808"/>
# <path d="M686.849 23.5415C689.098 17.3785 691.034 11.5166 693.368 5.80656C693.898 4.51356 695.78 2.93655 697.098 2.88355C704.289 2.59755 711.498 2.74757 719.463 2.74757C716.496 10.8056 713.844 18.0865 711.137 25.3485C704.791 42.3785 698.265 59.3506 692.199 76.4746C691.138 79.4706 691.036 83.4016 692.074 86.3836C701.386 113.128 711.052 139.756 720.89 167.192C711.592 166.126 702.837 165.244 694.145 163.962C693.125 163.812 692.155 161.554 691.663 160.112C686.109 143.868 680.655 127.591 675.168 111.325C674.704 109.948 674.193 108.586 673.283 106.04L653.271 159.96L628.292 157.497C630.335 152.162 632.169 147.257 634.091 142.383C641.799 122.831 649.627 103.323 657.139 83.6986C658.041 81.3396 658.06 78.1146 657.18 75.7476C648.691 52.9336 639.919 30.2176 631.241 7.47056C630.663 5.95456 630.191 4.40056 629.598 2.65656C638.432 2.65656 646.824 2.51655 655.201 2.81455C656.389 2.85755 658.052 4.83655 658.556 6.23655C663.812 20.8245 668.874 35.4795 673.998 50.1115C674.437 51.3625 674.945 52.5906 675.714 54.5916C679.532 43.9016 683.106 33.8995 686.849 23.5415ZM103.409 127.229V2.66355H175.946V23.6736H130.588V63.7906H166.37V84.7185L130.471 86.2846V132.881L175.509 130.027V151.262L103.408 156.727V127.229H103.409Z" fill="#E00909"/>
# <path d="M279.618 2.51057H349.727V22.5356H306.704V62.1405H340.385V82.9016H306.173V145.452H279.618V2.51057Z" fill="#E00808"/>
# <path d="M238.666 147.718L212.348 148.977V23.3716H184.922V2.50856H266.468V22.9296H238.668C238.668 59.5415 238.668 95.6326 238.666 132.224V147.718Z" fill="#E00A0A"/>
# <path d="M430.54 145.669C407.947 145.657 385.805 145.657 363.341 145.657V2.43855H389.574V124.639H433.619C433.619 131.63 433.683 137.889 433.505 144.139C433.489 144.675 431.866 145.168 430.54 145.669Z" fill="#E00707"/>
# </g>
# </svg>



# 