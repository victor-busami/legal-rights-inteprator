from langdetect import detect
from typing import Optional

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """Translate text between languages using a simple dictionary approach"""
    try:
        if source_lang == target_lang:
            return text
        
        # Simple translation dictionary for common legal terms
        translations = {
            'en': {
                'es': {
                    'rights': 'derechos',
                    'law': 'ley',
                    'legal': 'legal',
                    'employment': 'empleo',
                    'work': 'trabajo',
                    'fired': 'despedido',
                    'discrimination': 'discriminación',
                    'harassment': 'acoso',
                    'wage': 'salario',
                    'overtime': 'horas extra',
                    'safety': 'seguridad',
                    'termination': 'terminación',
                    'contract': 'contrato',
                    'court': 'tribunal',
                    'judge': 'juez',
                    'attorney': 'abogado',
                    'lawsuit': 'demanda',
                    'damages': 'daños',
                    'compensation': 'compensación',
                    'divorce': 'divorcio',
                    'custody': 'custodia',
                    'child support': 'manutención infantil',
                    'property': 'propiedad',
                    'landlord': 'propietario',
                    'tenant': 'inquilino',
                    'rent': 'alquiler',
                    'eviction': 'desalojo'
                },
                'fr': {
                    'rights': 'droits',
                    'law': 'loi',
                    'legal': 'légal',
                    'employment': 'emploi',
                    'work': 'travail',
                    'fired': 'licencié',
                    'discrimination': 'discrimination',
                    'harassment': 'harcèlement',
                    'wage': 'salaire',
                    'overtime': 'heures supplémentaires',
                    'safety': 'sécurité',
                    'termination': 'licenciement',
                    'contract': 'contrat',
                    'court': 'tribunal',
                    'judge': 'juge',
                    'attorney': 'avocat',
                    'lawsuit': 'procès',
                    'damages': 'dommages',
                    'compensation': 'compensation',
                    'divorce': 'divorce',
                    'custody': 'garde',
                    'child support': 'pension alimentaire',
                    'property': 'propriété',
                    'landlord': 'propriétaire',
                    'tenant': 'locataire',
                    'rent': 'loyer',
                    'eviction': 'expulsion'
                },
                'de': {
                    'rights': 'Rechte',
                    'law': 'Gesetz',
                    'legal': 'rechtlich',
                    'employment': 'Beschäftigung',
                    'work': 'Arbeit',
                    'fired': 'gekündigt',
                    'discrimination': 'Diskriminierung',
                    'harassment': 'Belästigung',
                    'wage': 'Lohn',
                    'overtime': 'Überstunden',
                    'safety': 'Sicherheit',
                    'termination': 'Kündigung',
                    'contract': 'Vertrag',
                    'court': 'Gericht',
                    'judge': 'Richter',
                    'attorney': 'Anwalt',
                    'lawsuit': 'Klage',
                    'damages': 'Schadensersatz',
                    'compensation': 'Entschädigung',
                    'divorce': 'Scheidung',
                    'custody': 'Sorgerecht',
                    'child support': 'Kindesunterhalt',
                    'property': 'Eigentum',
                    'landlord': 'Vermieter',
                    'tenant': 'Mieter',
                    'rent': 'Miete',
                    'eviction': 'Räumung'
                }
            }
        }
        
        # Get translation dictionary for the language pair
        lang_dict = translations.get(source_lang, {}).get(target_lang, {})
        
        # Simple word-by-word translation
        translated_text = text
        for english_word, translated_word in lang_dict.items():
            translated_text = translated_text.replace(english_word, translated_word)
            translated_text = translated_text.replace(english_word.title(), translated_word.title())
        
        return translated_text
        
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def detect_language(text: str) -> Optional[str]:
    """Detect the language of input text"""
    try:
        detected = detect(text)
        return detected
    except Exception as e:
        print(f"Language detection error: {e}")
        return None

def get_supported_languages() -> dict:
    """Get list of supported languages"""
    return {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'zh': 'Chinese',
        'ja': 'Japanese',
        'ko': 'Korean',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'bn': 'Bengali',
        'ur': 'Urdu',
        'tr': 'Turkish',
        'nl': 'Dutch',
        'sv': 'Swedish',
        'no': 'Norwegian',
        'da': 'Danish',
        'fi': 'Finnish'
    }

def translate_legal_terms(domain: str, target_lang: str) -> str:
    """Translate legal domain-specific terms"""
    legal_terms = {
        'Labor Law': {
            'en': 'Labor Law',
            'es': 'Derecho Laboral',
            'fr': 'Droit du Travail',
            'de': 'Arbeitsrecht',
            'it': 'Diritto del Lavoro',
            'pt': 'Direito do Trabalho'
        },
        'Criminal Law': {
            'en': 'Criminal Law',
            'es': 'Derecho Penal',
            'fr': 'Droit Pénal',
            'de': 'Strafrecht',
            'it': 'Diritto Penale',
            'pt': 'Direito Penal'
        },
        'Civil Law': {
            'en': 'Civil Law',
            'es': 'Derecho Civil',
            'fr': 'Droit Civil',
            'de': 'Zivilrecht',
            'it': 'Diritto Civile',
            'pt': 'Direito Civil'
        },
        'Family Law': {
            'en': 'Family Law',
            'es': 'Derecho de Familia',
            'fr': 'Droit de la Famille',
            'de': 'Familienrecht',
            'it': 'Diritto di Famiglia',
            'pt': 'Direito de Família'
        },
        'Property Law': {
            'en': 'Property Law',
            'es': 'Derecho de Propiedad',
            'fr': 'Droit de la Propriété',
            'de': 'Eigentumsrecht',
            'it': 'Diritto di Proprietà',
            'pt': 'Direito de Propriedade'
        }
    }
    
    return legal_terms.get(domain, {}).get(target_lang, domain) 