#!/usr/bin/env python3
import os
import glob

# Language configurations
LANGUAGES = {
    'en': {
        'title': 'Inventory.AI - Smart Garage Inventory Management',
        'header': '📦 Inventory.AI',
        'tagline': 'Smart Garage Inventory Management',
        'main_title': 'Never Lose Track of Your Items Again',
        'description': 'Inventory.AI helps you organize and manage items stored in boxes. With AI-powered image recognition, QR code generation, and cloud sync, keeping track of your belongings has never been easier.',
        'features_title': 'Key Features',
        'screenshots_title': 'App Screenshots',
        'links_title': 'Quick Links',
        'appstore_button': 'Download on the App Store',
        'appstore_country': 'us',
        'features': [
            ('📸', 'Photo Recognition', 'AI-powered analysis identifies objects, colors, and materials in your photos'),
            ('📦', 'Box Organization', 'Create and manage storage boxes with unique identifiers and QR codes'),
            ('☁️', 'Cloud Sync', 'Optional cloud backup to access your inventory from any device'),
            ('🔍', 'Smart Search', 'Quickly find items by name, box, or description'),
            ('📄', 'PDF Export', 'Generate printable reports with QR codes for your boxes'),
            ('🌙', 'Beautiful Design', 'Clean, modern interface with dark mode support')
        ],
        'links': [
            ('Support', 'support-en.html'),
            ('Privacy Policy', 'privacy-en.html'),
            ('Terms & Conditions', 'terms-en.html')
        ],
        'folder': 'en'
    },
    'it': {
        'title': 'Inventory.AI - Gestione Intelligente dell\'Inventario',
        'header': '📦 Inventory.AI',
        'tagline': 'Gestione Intelligente dell\'Inventario del Garage',
        'main_title': 'Non Perdere Mai Traccia dei Tuoi Oggetti',
        'description': 'Inventory.AI ti aiuta a organizzare e gestire gli oggetti conservati nelle scatole. Con riconoscimento immagini AI, generazione di codici QR e sincronizzazione cloud, tenere traccia dei tuoi beni non è mai stato così facile.',
        'features_title': 'Funzionalità Principali',
        'screenshots_title': 'Schermate dell\'App',
        'links_title': 'Link Rapidi',
        'appstore_button': 'Scarica dall\'App Store',
        'appstore_country': 'it',
        'features': [
            ('📸', 'Riconoscimento Foto', 'L\'analisi AI identifica oggetti, colori e materiali nelle tue foto'),
            ('📦', 'Organizzazione Scatole', 'Crea e gestisci scatole con identificatori unici e codici QR'),
            ('☁️', 'Sincronizzazione Cloud', 'Backup cloud opzionale per accedere al tuo inventario da qualsiasi dispositivo'),
            ('🔍', 'Ricerca Intelligente', 'Trova rapidamente gli oggetti per nome, scatola o descrizione'),
            ('📄', 'Esportazione PDF', 'Genera report stampabili con codici QR per le tue scatole'),
            ('🌙', 'Design Elegante', 'Interfaccia moderna e pulita con supporto modalità scura')
        ],
        'links': [
            ('Supporto', 'support-it.html'),
            ('Privacy Policy', 'privacy-it.html'),
            ('Termini e Condizioni', 'terms-it.html')
        ],
        'folder': 'it'
    },
    'de': {
        'title': 'Inventory.AI - Intelligente Garagenverwaltung',
        'header': '📦 Inventory.AI',
        'tagline': 'Intelligente Garagenverwaltung',
        'main_title': 'Verlieren Sie Nie Wieder Den Überblick',
        'description': 'Inventory.AI hilft Ihnen, in Kartons gelagerte Gegenstände zu organisieren und zu verwalten. Mit KI-gestützter Bilderkennung, QR-Code-Generierung und Cloud-Synchronisierung war es noch nie so einfach, den Überblick über Ihre Sachen zu behalten.',
        'features_title': 'Hauptfunktionen',
        'screenshots_title': 'App-Screenshots',
        'links_title': 'Schnelllinks',
        'appstore_button': 'Laden im App Store',
        'appstore_country': 'de',
        'features': [
            ('📸', 'Fotoerkennung', 'KI-gestützte Analyse identifiziert Objekte, Farben und Materialien'),
            ('📦', 'Kartonverwaltung', 'Erstellen und verwalten Sie Kartons mit eindeutigen IDs und QR-Codes'),
            ('☁️', 'Cloud-Sync', 'Optionales Cloud-Backup für Zugriff von jedem Gerät'),
            ('🔍', 'Intelligente Suche', 'Finden Sie schnell Artikel nach Name, Karton oder Beschreibung'),
            ('📄', 'PDF-Export', 'Erstellen Sie druckbare Berichte mit QR-Codes für Ihre Kartons'),
            ('🌙', 'Schönes Design', 'Saubere, moderne Oberfläche mit Dark-Mode-Unterstützung')
        ],
        'links': [
            ('Support', 'support-de.html'),
            ('Datenschutz', 'privacy-de.html'),
            ('AGB', 'terms-de.html')
        ],
        'folder': 'de'
    },
    'es': {
        'title': 'Inventory.AI - Gestión Inteligente de Inventario',
        'header': '📦 Inventory.AI',
        'tagline': 'Gestión Inteligente de Inventario de Garaje',
        'main_title': 'Nunca Pierdas el Rastro de Tus Artículos',
        'description': 'Inventory.AI te ayuda a organizar y gestionar artículos almacenados en cajas. Con reconocimiento de imágenes con IA, generación de códigos QR y sincronización en la nube, llevar un seguimiento de tus pertenencias nunca ha sido tan fácil.',
        'features_title': 'Características Principales',
        'screenshots_title': 'Capturas de la App',
        'links_title': 'Enlaces Rápidos',
        'appstore_button': 'Descargar en App Store',
        'appstore_country': 'es',
        'features': [
            ('📸', 'Reconocimiento de Fotos', 'El análisis con IA identifica objetos, colores y materiales en tus fotos'),
            ('📦', 'Organización de Cajas', 'Crea y gestiona cajas con identificadores únicos y códigos QR'),
            ('☁️', 'Sincronización en la Nube', 'Copia de seguridad opcional para acceder a tu inventario desde cualquier dispositivo'),
            ('🔍', 'Búsqueda Inteligente', 'Encuentra rápidamente artículos por nombre, caja o descripción'),
            ('📄', 'Exportar a PDF', 'Genera informes imprimibles con códigos QR para tus cajas'),
            ('🌙', 'Diseño Hermoso', 'Interfaz limpia y moderna con soporte para modo oscuro')
        ],
        'links': [
            ('Soporte', 'support-es.html'),
            ('Política de Privacidad', 'privacy-es.html'),
            ('Términos y Condiciones', 'terms-es.html')
        ],
        'folder': 'es'
    },
    'fr': {
        'title': 'Inventory.AI - Gestion Intelligente d\'Inventaire',
        'header': '📦 Inventory.AI',
        'tagline': 'Gestion Intelligente d\'Inventaire de Garage',
        'main_title': 'Ne Perdez Plus Jamais La Trace de Vos Objets',
        'description': 'Inventory.AI vous aide à organiser et gérer les objets stockés dans des boîtes. Avec la reconnaissance d\'images par IA, la génération de codes QR et la synchronisation cloud, garder une trace de vos affaires n\'a jamais été aussi facile.',
        'features_title': 'Fonctionnalités Principales',
        'screenshots_title': 'Captures d\'Écran',
        'links_title': 'Liens Rapides',
        'appstore_button': 'Télécharger sur l\'App Store',
        'appstore_country': 'fr',
        'features': [
            ('📸', 'Reconnaissance Photo', 'L\'analyse IA identifie les objets, couleurs et matériaux dans vos photos'),
            ('📦', 'Organisation des Boîtes', 'Créez et gérez des boîtes avec identifiants uniques et codes QR'),
            ('☁️', 'Synchronisation Cloud', 'Sauvegarde cloud optionnelle pour accéder à votre inventaire depuis n\'importe quel appareil'),
            ('🔍', 'Recherche Intelligente', 'Trouvez rapidement des articles par nom, boîte ou description'),
            ('📄', 'Export PDF', 'Générez des rapports imprimables avec codes QR pour vos boîtes'),
            ('🌙', 'Design Élégant', 'Interface propre et moderne avec support du mode sombre')
        ],
        'links': [
            ('Support', 'support-fr.html'),
            ('Politique de Confidentialité', 'privacy-fr.html'),
            ('Conditions d\'Utilisation', 'terms-fr.html')
        ],
        'folder': 'fr'
    },
    'ja': {
        'title': 'Inventory.AI - スマート在庫管理',
        'header': '📦 Inventory.AI',
        'tagline': 'スマートガレージ在庫管理',
        'main_title': 'アイテムを二度と見失わない',
        'description': 'Inventory.AIは、ボックスに保管されたアイテムの整理と管理を支援します。AI搭載の画像認識、QRコード生成、クラウド同期により、持ち物の追跡がこれまでになく簡単になりました。',
        'features_title': '主な機能',
        'screenshots_title': 'アプリのスクリーンショット',
        'links_title': 'クイックリンク',
        'appstore_button': 'App Storeからダウンロード',
        'appstore_country': 'jp',
        'features': [
            ('📸', '写真認識', 'AI分析が写真内の物体、色、素材を識別します'),
            ('📦', 'ボックス整理', '固有の識別子とQRコードでボックスを作成・管理'),
            ('☁️', 'クラウド同期', 'オプションのクラウドバックアップで、どのデバイスからでも在庫にアクセス'),
            ('🔍', 'スマート検索', '名前、ボックス、説明でアイテムを素早く検索'),
            ('📄', 'PDF出力', 'ボックス用のQRコード付き印刷可能レポートを生成'),
            ('🌙', '美しいデザイン', 'ダークモード対応のクリーンでモダンなインターフェース')
        ],
        'links': [
            ('サポート', 'support-ja.html'),
            ('プライバシーポリシー', 'privacy-ja.html'),
            ('利用規約', 'terms-ja.html')
        ],
        'folder': 'ja'
    },
    'ko': {
        'title': 'Inventory.AI - 스마트 재고 관리',
        'header': '📦 Inventory.AI',
        'tagline': '스마트 차고 재고 관리',
        'main_title': '물건을 다시는 잃어버리지 마세요',
        'description': 'Inventory.AI는 상자에 보관된 물품을 정리하고 관리하는 데 도움을 줍니다. AI 기반 이미지 인식, QR 코드 생성, 클라우드 동기화를 통해 소지품을 추적하는 것이 그 어느 때보다 쉬워졌습니다.',
        'features_title': '주요 기능',
        'screenshots_title': '앱 스크린샷',
        'links_title': '빠른 링크',
        'appstore_button': 'App Store에서 다운로드',
        'appstore_country': 'kr',
        'features': [
            ('📸', '사진 인식', 'AI 분석이 사진 속 물체, 색상, 재질을 식별합니다'),
            ('📦', '상자 정리', '고유 식별자와 QR 코드로 보관 상자를 생성하고 관리하세요'),
            ('☁️', '클라우드 동기화', '모든 기기에서 재고에 액세스할 수 있는 선택적 클라우드 백업'),
            ('🔍', '스마트 검색', '이름, 상자 또는 설명으로 품목을 빠르게 찾기'),
            ('📄', 'PDF 내보내기', '상자용 QR 코드가 포함된 인쇄 가능한 보고서 생성'),
            ('🌙', '아름다운 디자인', '다크 모드를 지원하는 깔끔하고 현대적인 인터페이스')
        ],
        'links': [
            ('지원', 'support-ko.html'),
            ('개인정보 처리방침', 'privacy-ko.html'),
            ('이용약관', 'terms-ko.html')
        ],
        'folder': 'ko'
    },
    'nl': {
        'title': 'Inventory.AI - Slimme Inventarisbeheer',
        'header': '📦 Inventory.AI',
        'tagline': 'Slim Garage Inventarisbeheer',
        'main_title': 'Verlies Nooit Meer Het Spoor Van Je Spullen',
        'description': 'Inventory.AI helpt je items die in dozen zijn opgeslagen te organiseren en beheren. Met AI-aangedreven beeldherkenning, QR-code generatie en cloud-synchronisatie was het bijhouden van je bezittingen nog nooit zo eenvoudig.',
        'features_title': 'Belangrijkste Functies',
        'screenshots_title': 'App Screenshots',
        'links_title': 'Snelle Links',
        'appstore_button': 'Download in de App Store',
        'appstore_country': 'nl',
        'features': [
            ('📸', 'Fotoherkenning', 'AI-analyse identificeert objecten, kleuren en materialen in je foto\'s'),
            ('📦', 'Doos Organisatie', 'Maak en beheer dozen met unieke ID\'s en QR-codes'),
            ('☁️', 'Cloud Sync', 'Optionele cloud backup om je inventaris vanaf elk apparaat te benaderen'),
            ('🔍', 'Slim Zoeken', 'Vind snel items op naam, doos of beschrijving'),
            ('📄', 'PDF Export', 'Genereer afdrukbare rapporten met QR-codes voor je dozen'),
            ('🌙', 'Mooi Design', 'Schone, moderne interface met ondersteuning voor donkere modus')
        ],
        'links': [
            ('Ondersteuning', 'support-nl.html'),
            ('Privacybeleid', 'privacy-nl.html'),
            ('Voorwaarden', 'terms-nl.html')
        ],
        'folder': 'nl'
    },
    'pt': {
        'title': 'Inventory.AI - Gestão Inteligente de Inventário',
        'header': '📦 Inventory.AI',
        'tagline': 'Gestão Inteligente de Inventário de Garagem',
        'main_title': 'Nunca Perca o Controle dos Seus Itens',
        'description': 'Inventory.AI ajuda você a organizar e gerenciar itens armazenados em caixas. Com reconhecimento de imagem por IA, geração de código QR e sincronização na nuvem, acompanhar seus pertences nunca foi tão fácil.',
        'features_title': 'Recursos Principais',
        'screenshots_title': 'Capturas de Tela',
        'links_title': 'Links Rápidos',
        'appstore_button': 'Baixar na App Store',
        'appstore_country': 'pt',
        'features': [
            ('📸', 'Reconhecimento de Fotos', 'Análise por IA identifica objetos, cores e materiais nas suas fotos'),
            ('📦', 'Organização de Caixas', 'Crie e gerencie caixas com identificadores únicos e códigos QR'),
            ('☁️', 'Sincronização na Nuvem', 'Backup opcional na nuvem para acessar seu inventário de qualquer dispositivo'),
            ('🔍', 'Busca Inteligente', 'Encontre rapidamente itens por nome, caixa ou descrição'),
            ('📄', 'Exportação PDF', 'Gere relatórios imprimíveis com códigos QR para suas caixas'),
            ('🌙', 'Design Bonito', 'Interface limpa e moderna com suporte a modo escuro')
        ],
        'links': [
            ('Suporte', 'support-pt.html'),
            ('Política de Privacidade', 'privacy-pt.html'),
            ('Termos e Condições', 'terms-pt.html')
        ],
        'folder': 'pt'
    },
    'ru': {
        'title': 'Inventory.AI - Умное Управление Инвентарём',
        'header': '📦 Inventory.AI',
        'tagline': 'Умное Управление Гаражным Инвентарём',
        'main_title': 'Никогда Не Теряйте Свои Вещи',
        'description': 'Inventory.AI помогает вам организовывать и управлять предметами, хранящимися в коробках. С распознаванием изображений на основе ИИ, генерацией QR-кодов и облачной синхронизацией отслеживание ваших вещей стало проще простого.',
        'features_title': 'Основные Возможности',
        'screenshots_title': 'Скриншоты Приложения',
        'links_title': 'Быстрые Ссылки',
        'appstore_button': 'Загрузить в App Store',
        'appstore_country': 'ru',
        'features': [
            ('📸', 'Распознавание Фото', 'Анализ на основе ИИ определяет объекты, цвета и материалы на ваших фотографиях'),
            ('📦', 'Организация Коробок', 'Создавайте и управляйте коробками с уникальными идентификаторами и QR-кодами'),
            ('☁️', 'Облачная Синхронизация', 'Дополнительное облачное резервное копирование для доступа к инвентарю с любого устройства'),
            ('🔍', 'Умный Поиск', 'Быстро находите предметы по имени, коробке или описанию'),
            ('📄', 'Экспорт в PDF', 'Создавайте печатные отчёты с QR-кодами для ваших коробок'),
            ('🌙', 'Красивый Дизайн', 'Чистый, современный интерфейс с поддержкой тёмной темы')
        ],
        'links': [
            ('Поддержка', 'support-ru.html'),
            ('Политика Конфиденциальности', 'privacy-ru.html'),
            ('Условия Использования', 'terms-ru.html')
        ],
        'folder': 'ru'
    },
    'zh': {
        'title': 'Inventory.AI - 智能库存管理',
        'header': '📦 Inventory.AI',
        'tagline': '智能车库库存管理',
        'main_title': '再也不会丢失您的物品',
        'description': 'Inventory.AI 帮助您整理和管理存放在盒子中的物品。通过AI驱动的图像识别、二维码生成和云同步，追踪您的物品从未如此简单。',
        'features_title': '主要功能',
        'screenshots_title': '应用截图',
        'links_title': '快速链接',
        'appstore_button': '在App Store下载',
        'appstore_country': 'cn',
        'features': [
            ('📸', '照片识别', 'AI分析识别照片中的物体、颜色和材料'),
            ('📦', '盒子整理', '使用唯一标识符和二维码创建和管理存储盒'),
            ('☁️', '云同步', '可选的云备份，从任何设备访问您的库存'),
            ('🔍', '智能搜索', '按名称、盒子或描述快速查找物品'),
            ('📄', 'PDF导出', '为您的盒子生成带有二维码的可打印报告'),
            ('🌙', '精美设计', '支持深色模式的简洁现代界面')
        ],
        'links': [
            ('支持', 'support-zh.html'),
            ('隐私政策', 'privacy-zh.html'),
            ('条款和条件', 'terms-zh.html')
        ],
        'folder': 'zh'
    }
}

def get_unique_images(folder):
    """Get unique images, preferring PNG over JPG"""
    if not os.path.exists(folder):
        return []

    all_images = glob.glob(f"{folder}/*.png") + glob.glob(f"{folder}/*.jpg") + glob.glob(f"{folder}/*.jpeg")

    # Group by base name (without extension)
    images_by_base = {}
    for img in all_images:
        base = os.path.splitext(os.path.basename(img))[0]
        ext = os.path.splitext(img)[1].lower()

        if base not in images_by_base:
            images_by_base[base] = []
        images_by_base[base].append((ext, img))

    # Select PNG over JPG/JPEG
    unique_images = []
    for base, variants in sorted(images_by_base.items()):
        # Sort by extension priority: .png first, then .jpg, then .jpeg
        variants.sort(key=lambda x: (0 if x[0] == '.png' else 1 if x[0] == '.jpg' else 2))
        unique_images.append(variants[0][1])

    return sorted(unique_images)

def generate_html(lang_code, config):
    """Generate HTML for a specific language"""

    # Generate App Store button HTML
    appstore_url = f"https://apps.apple.com/{config['appstore_country']}/app/inventory-ai/id6757914537"
    appstore_html = f'''
        <div class="appstore-section">
            <a href="{appstore_url}" class="appstore-button" target="_blank" rel="noopener">
                <span class="appstore-icon">📱</span>{config['appstore_button']}
            </a>
        </div>
'''

    # Get screenshots for this language
    screenshots = get_unique_images(config['folder'])
    screenshots_html = ""

    if screenshots:
        screenshots_html = f'''
        <div class="screenshots-section">
            <h2>{config['screenshots_title']}</h2>
            <div class="screenshots-container">
'''
        for screenshot in screenshots:
            screenshots_html += f'                <img src="{screenshot}" alt="Screenshot" class="screenshot">\n'

        screenshots_html += '''            </div>
        </div>
'''

    # Generate features HTML
    features_html = ""
    for emoji, title, description in config['features']:
        features_html += f'''                <div class="feature">
                    <div class="feature-icon">{emoji}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
'''

    # Generate links HTML
    links_html = ""
    for link_text, link_url in config['links']:
        links_html += f'                <a href="{link_url}" class="link-button">{link_text}</a>\n'

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{config['description'][:150]}">
    <title>{config['title']}</title>

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">

    <!-- Open Graph / Social Media -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{config['title']}">
    <meta property="og:description" content="{config['description'][:150]}">
    <meta property="og:image" content="app-icon-1024.png">
    <meta property="og:url" content="https://yourdomain.com/index-{lang_code}.html">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{config['title']}">
    <meta name="twitter:description" content="{config['description'][:150]}">
    <meta name="twitter:image" content="app-icon-1024.png">

    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f7fa;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        header {{
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            margin-bottom: 40px;
        }}

        .app-icon {{
            width: 120px;
            height: 120px;
            border-radius: 25px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }}

        h1 {{
            font-size: 3em;
            margin-bottom: 10px;
        }}

        .tagline {{
            font-size: 1.2em;
            opacity: 0.95;
        }}

        .content-card {{
            background: white;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .content-card h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2em;
        }}

        .content-card > p {{
            font-size: 1.1em;
            margin-bottom: 30px;
            color: #555;
        }}

        .features {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }}

        .feature {{
            text-align: center;
            padding: 20px;
        }}

        .feature-icon {{
            font-size: 3em;
            margin-bottom: 15px;
        }}

        .feature h3 {{
            color: #764ba2;
            margin-bottom: 10px;
            font-size: 1.3em;
        }}

        .feature p {{
            color: #666;
            font-size: 0.95em;
        }}

        .screenshots-section {{
            background: white;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .screenshots-section h2 {{
            color: #667eea;
            margin-bottom: 30px;
            font-size: 2em;
            text-align: center;
        }}

        .screenshots-container {{
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 20px 0;
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
        }}

        .screenshots-container::-webkit-scrollbar {{
            height: 8px;
        }}

        .screenshots-container::-webkit-scrollbar-track {{
            background: #f1f1f1;
            border-radius: 10px;
        }}

        .screenshots-container::-webkit-scrollbar-thumb {{
            background: #667eea;
            border-radius: 10px;
        }}

        .screenshot {{
            flex: 0 0 auto;
            height: 500px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .screenshot:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }}

        .appstore-section {{
            text-align: center;
            padding: 60px 40px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .appstore-button {{
            display: inline-block;
            padding: 18px 50px;
            background: #000;
            color: white !important;
            text-decoration: none;
            border-radius: 12px;
            font-size: 1.3em;
            font-weight: 600;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}

        .appstore-button:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }}

        .appstore-icon {{
            font-size: 1.5em;
            margin-right: 10px;
            vertical-align: middle;
        }}

        .links {{
            text-align: center;
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .links h2 {{
            color: #667eea;
            margin-bottom: 20px;
        }}

        .link-button {{
            display: inline-block;
            margin: 10px;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            text-decoration: none;
            border-radius: 8px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            font-weight: 500;
        }}

        .link-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}

        @media (max-width: 768px) {{
            .app-icon {{
                width: 90px;
                height: 90px;
                border-radius: 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            .content-card {{
                padding: 30px 20px;
            }}

            .appstore-section {{
                padding: 40px 20px;
            }}

            .appstore-button {{
                font-size: 1.1em;
                padding: 15px 35px;
            }}

            .screenshots-section {{
                padding: 30px 20px;
            }}

            .screenshot {{
                height: 400px;
            }}

            .features {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <img src="app-icon-512.png" alt="Inventory.AI Icon" class="app-icon">
            <h1>{config['header']}</h1>
            <p class="tagline">{config['tagline']}</p>
        </header>

        <div class="content-card">
            <h2>{config['main_title']}</h2>
            <p>{config['description']}</p>

            <h2 style="margin-top: 40px;">{config['features_title']}</h2>
            <div class="features">
{features_html}            </div>
        </div>

{appstore_html}
{screenshots_html}
        <div class="links">
            <h2>{config['links_title']}</h2>
{links_html}        </div>
    </div>
</body>
</html>
'''

    return html

def main():
    """Generate all index pages"""
    for lang_code, config in LANGUAGES.items():
        filename = f"index-{lang_code}.html"
        html_content = generate_html(lang_code, config)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✓ Generated {filename}")

    print(f"\n✓ Successfully generated {len(LANGUAGES)} index pages!")

if __name__ == '__main__':
    main()
