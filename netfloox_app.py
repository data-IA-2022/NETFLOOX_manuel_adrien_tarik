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
    # Define your javascript
    
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
                            <div class="logo">
                                <img src="https://github.com/data-IA-2022/NETFLOOX_manuel_adrien_tarik/blob/main/assets/netfloox_logo.png?raw=true" class="logo">
                            </div>
                                <div class="our-story-header our-story-header--has-language-selector" data-uia-nmhp="our-story-header">
                                    <div class="lang-selection-container" id="lang-switcher"><div data-uia="language-picker-header+container" class="ui-select-wrapper">
                                        <label for="lang-switcher-header-select" class="ui-label">
                                            <span class="ui-label-text">Choisir la langue</span>
                                        </label>
                                        <div class="select-arrow medium prefix globe">
                                            <select data-uia="language-picker-header" class="ui-select medium" id="lang-switcher-header-select" tabindex="0" placeholder="lang-switcher">
                                                <option selected="" lang="fr" value="/fr/" data-language="fr" data-country="FR">Français</option>
                                                <option lang="en" value="/fr-en/" data-language="en" data-country="FR">English</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>  
                            <a href="/login" class="authLinks redButton" data-uia="header-login-link">S'identifier</a>                
                        </nav>
                        <div class="header-content">
                            <h1>Films, séries et bien plus en illimité.</h1>
                            <h2>Où que vous soyez. Annulez à tout moment.</h2>
                            <p>Prêt à regarder Netfloox ? Saisissez votre adresse e-mail pour vous abonner ou réactiver votre abonnement.</p>
                            <form class="email-signup">
                                <input type="email" placeholder="Adresse e-mail" required>
                                <button type="submit">Commencer<svg viewBox="0 0 6 12" xmlns="http://www.w3.org/2000/svg"><desc>chevron</desc><path d="M.61 1.312l.78-.624L5.64 6l-4.25 5.312-.78-.624L4.36 6z" fill="none" fill-rule="evenodd"></path></svg></button>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="our-story-card animation-card watchOnTv" data-uia-nmhp="watchOnTv" data-uia="our-story-card">
                    <div class="animation-card-container">
                        <div class="our-story-card-text">
                            <h1 id="" class="our-story-card-title" data-uia="animation-card-title">Regardez Netfloox sur votre&nbsp;TV.</h1>
                            <h2 id="" class="our-story-card-subtitle" data-uia="our-story-card-subtitle">Regardez Netfloox sur votre Smart&nbsp;TV, PlayStation, Xbox, Chromecast, Apple&nbsp;TV, lecteur Blu-ray et&nbsp;bien plus.</h2></div>
                                <div class="our-story-card-img-container"><div class="our-story-card-animation-container">
                                    <img alt="" class="our-story-card-img" src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/tv.png" data-uia="our-story-card-img">
                                        <div class="our-story-card-animation" data-uia="our-story-card-animation"><video class="our-story-card-video" data-uia="our-story-card-video" autoplay="" playsinline="" muted="" loop="">
                                            <source src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/video-tv-0819.m4v" type="video/mp4"></video><div class="our-story-card-animation-text">
                                        </div>
                                        <div class="our-story-card-animation-custom" data-uia="our-story-card-custom" aria-hidden="true">
                                        </div>
                                </div>
                        </div>
                    </div>
                    <div class="center-pixel" style="position:absolute">
                    </div>
                </div>
                <div class="our-story-card animation-card watchOnDevice flipped" data-uia-nmhp="watchOnDevice" data-uia="our-story-card">
                    <div class="animation-card-container">
                        <div class="our-story-card-text">
                            <h1 id="" class="our-story-card-title" data-uia="animation-card-title">Où que vous soyez.</h1>
                            <h2 id="" class="our-story-card-subtitle" data-uia="our-story-card-subtitle">Regardez des films et séries en illimité sur votre TV, smartphone, tablette et ordinateur, sans payer de supplément.</h2>
                        </div>
                        <div class="our-story-card-img-container">
                            <div class="our-story-card-animation-container"><img alt="" class="our-story-card-img" src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/device-pile.png" data-uia="our-story-card-img">
                                <div class="our-story-card-animation" data-uia="our-story-card-animation">
                                    <video class="our-story-card-video" data-uia="our-story-card-video" autoplay="" playsinline="" muted="" loop="">
                                        <source src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/video-devices.m4v" type="video/mp4">
                                    </video>
                                        <div class="our-story-card-animation-text">
                                        </div>
                                        <div class="our-story-card-animation-custom" data-uia="our-story-card-custom" aria-hidden="true">
                                        </div>
                                </div>
                            </div>
                        </div>
                        <div class="center-pixel" style="position:absolute">
                    </div>
                </div>
                </div>
                <div class="our-story-card animation-card kidsValueProp" data-uia-nmhp="kidsValueProp" data-uia="our-story-card"><div class="animation-card-container"><div class="our-story-card-text"><h1 id="" class="our-story-card-title" data-uia="animation-card-title">Créez des profils pour les enfants.</h1><h2 id="" class="our-story-card-subtitle" data-uia="our-story-card-subtitle">Les enfants découvrent de nouvelles aventures et retrouvent leurs personnages préférés dans un espace bien à eux, déjà inclus dans votre abonnement.</h2></div><div class="our-story-card-img-container"><div class="our-story-card-animation-container"><img alt="" class="our-story-card-img" src="https://occ-0-6613-769.1.nflxso.net/dnm/api/v6/19OhWN2dO19C9txTON9tvTFtefw/AAAABbN6pi_bFc9A7RIro_XUCRVuEb-PNbPx2G8CMhztwzwCRI6k5QsMd_qUPPkb89KSQwBFg0ijdx88drv37Y4unvXzCjB-V0vIk3mP.png?r=a3e" data-uia="our-story-card-img"><div class="our-story-card-animation" data-uia="our-story-card-animation"><div class="our-story-card-animation-text"></div><div class="our-story-card-animation-custom" data-uia="our-story-card-custom" aria-hidden="true"></div></div></div></div><div class="center-pixel" style="position:absolute"></div></div></div>
                <div class="our-story-card animation-card downloadAndWatch flipped" data-uia-nmhp="downloadAndWatch" data-uia="our-story-card"><div class="animation-card-container"><div class="our-story-card-text"><h1 id="" class="our-story-card-title" data-uia="animation-card-title">Téléchargez vos séries préférées pour les regarder hors connexion.</h1><h2 id="" class="our-story-card-subtitle" data-uia="our-story-card-subtitle">Disponible avec toutes les offres, sauf Essentiel avec pub.</h2></div><div class="our-story-card-img-container"><div class="our-story-card-animation-container"><img alt="" class="our-story-card-img" src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/mobile-0819.jpg" data-uia="our-story-card-img"><div class="our-story-card-animation" data-uia="our-story-card-animation"><div class="our-story-card-animation-image"><img alt="" src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/boxshot.png"></div><div class="our-story-card-animation-text"><div id="" class="text-0" data-uia="">Stranger Things</div><div id="" class="text-1" data-uia="">Téléchargement en cours...</div></div><div class="our-story-card-animation-custom" data-uia="our-story-card-custom" aria-hidden="true"></div></div></div></div><div class="center-pixel" style="position:absolute"></div></div></div>
                <div class="faq">
                    <h2>Foire aux questions</h2>
                    <ul class="accordion">
                        <li>
                            <input type="radio" name="accordion" id="first">
                            <label for="first">Netfloox, qu'est-ce que c'est ?</label>
                            <div class="content">
                                <p>Netfloox est un système de recommandation de contenu vidéo.<br>Le projet</p>
                            </div>
                        </li>
                        <li>
                            <input type="radio" name="accordion" id="second">
                            <label for="second">Netfloox, qu'est-ce que c'est ?</label>
                            <div class="content">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit cumque odio, totam eum culpa, laudantium nobis illo dolorem recusandae tempore vel animi, cupiditate impedit perferendis ratione aliquid numquam fugit temporibus.</p>
                            </div>
                        </li>
                        <li>
                            <input type="radio" name="accordion" id="third">
                            <label for="third">Netfloox, qu'est-ce que c'est ?</label>
                            <div class="content">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit cumque odio, totam eum culpa, laudantium nobis illo dolorem recusandae tempore vel animi, cupiditate impedit perferendis ratione aliquid numquam fugit temporibus.</p>
                            </div>
                        </li>
                        <li>
                            <input type="radio" name="accordion" id="fourth">
                            <label for="fourth">Netfloox, qu'est-ce que c'est ?</label>
                            <div class="content">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit cumque odio, totam eum culpa, laudantium nobis illo dolorem recusandae tempore vel animi, cupiditate impedit perferendis ratione aliquid numquam fugit temporibus.</p>
                            </div>
                        </li>
                        <li>
                            <input type="radio" name="accordion" id="fith">
                            <label for="fith">Netfloox, qu'est-ce que c'est ?</label>
                            <div class="content">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit cumque odio, totam eum culpa, laudantium nobis illo dolorem recusandae tempore vel animi, cupiditate impedit perferendis ratione aliquid numquam fugit temporibus.</p>
                            </div>
                        </li>
                    </ul>
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