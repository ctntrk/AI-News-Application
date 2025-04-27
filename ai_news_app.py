import streamlit as st
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

# Add cache to improve performance
@st.cache_data(ttl=3600)  # 1 hour cache
def fetch_ai_news(selected_sources, search_query=None):
    rss_urls = {
        "TechCrunch": "https://techcrunch.com/feed/",
        "MIT Technology Review": "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
        "Science Daily": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml",
        'Deepmind':'https://deepmind.google/blog/rss.xml',
        "Berkeley AI Research (BAIR) Blog":'https://bair.berkeley.edu/blog/feed.xml',
    }

    all_news = []
    for source_name, url in rss_urls.items():
        if source_name not in selected_sources:
            continue
            
        try:
            feed = feedparser.parse(url)
            if not hasattr(feed, 'entries') or len(feed.entries) == 0:
                st.warning(f"❗ {source_name} returned empty or invalid format")
                continue

            for entry in feed.entries[:5]:
                # Date filter
                pub_date = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else None
                
                # HTML cleaning
                summary = entry.get("summary", entry.get('description', "Summary not available"))
                soup = BeautifulSoup(summary, 'html.parser')
                clean_summary = soup.get_text()
                
                
                news_item = {
                    "title": entry.title,
                    "summary": clean_summary,
                    "link": entry.link,
                    "source": source_name,
                    "date": pub_date,
                    
                }
                
                # Search filter
                if search_query:
                    search_lower = search_query.lower()
                    if (search_lower not in news_item['title'].lower() and 
                        search_lower not in news_item['summary'].lower()):
                        continue
                
                all_news.append(news_item)
        except Exception as e:
            st.error(f"⛔ Error ({source_name}): {str(e)}")

    return all_news[:25]


# Main application
def main():
    st.set_page_config(
        page_title="AI News Aggregator Pro",
        page_icon="🤖",
        layout="wide"
    )

    # Header
    st.title("🤖 AI News Aggregator Pro")
    
    # Top filters
    col1, col2, col3 = st.columns([2,2,1])
    with col1:
        search_query = st.text_input("🔍 Search News")
    with col2:
        days_filter = st.slider("⏳ News from the last how many days?", 1, 30, 7)
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Refresh"):
            st.rerun()

    # Sidebar
    
    with st.sidebar:
        
        with st.expander("ℹ️ About the Project"):
            st.markdown("""
            **AI News Aggregator Pro**  
    

            **Purpose:**  
            📰 Real-time collection of AI-related news from trusted sources

            **Main Features:**  
            - 🕒 Automatic daily updates (1 hour cache)
            - 🔍 Keyword search functionality
            - ⏳ Time filter (1-30 days)
            - 📊 Source-based statistics
            - 📱 Mobile-friendly responsive design

            **Technologies Used:**  
            - Python
            - Streamlit (Web framework)
            - Feedparser (RSS processing)
            - BeautifulSoup (HTML cleaning)

            **Data Sources:**  
            - TechCrunch
            - MIT Technology Review 
            - Science Daily
            - DeepMind Blog
            - BAIR Blog

            """)

        st.markdown("---")

        st.header("Filters")
        sources = [
            "Deepmind",
            "TechCrunch", 
            "MIT Technology Review",
            "Science Daily",
            "Berkeley AI Research (BAIR) Blog",
        ]
        selected_sources = st.multiselect(
            "Select News Sources",
            options=sources,
            default=sources
        )



    # Load news
    with st.spinner(f"Loading news... {st.session_state.get('refresh_count', 1)}"):
        ai_news = fetch_ai_news(selected_sources, search_query)
        
        # Apply date filter
        cutoff_date = datetime.now() - timedelta(days=days_filter)
        ai_news = [news for news in ai_news if news['date'] and news['date'] > cutoff_date]

    # Statistics
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### 📊 Statistics")
    st.sidebar.markdown(f"Total News: {len(ai_news)}")
    source_counts = {source:0 for source in selected_sources}
    for news in ai_news:
        source_counts[news['source']] += 1
        
    # Büyükten küçüğe sıralama
    sorted_counts = sorted(source_counts.items(), key=lambda x: x[1], reverse=True)
    
    for source, count in sorted_counts:
        st.sidebar.markdown(f"- {source}: {count}")


    # Display news
    if not ai_news:
        st.warning("No news found matching your criteria.")
    else:
        cols = st.columns(2)
        for index, news in enumerate(ai_news):
            with cols[index % 2]:
                with st.container(border=True):
                    
                    st.markdown(f"### {news['title']}")
                    st.caption(f"**{news['source']}** - {news['date'].strftime('%d/%m/%Y %H:%M') if news['date'] else 'No date'}")
                    
                    with st.expander("View Summary"):
                        st.write(news['summary'])
                    
                    st.link_button("Go to Article →", news['link'])
                    st.markdown("---")

if __name__ == "__main__":
    main()
