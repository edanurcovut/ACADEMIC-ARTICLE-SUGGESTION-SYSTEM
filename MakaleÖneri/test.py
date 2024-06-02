def calculate_precision_recall(selected_articles, recommended_articles, top_n=5):
    # Seçilen makalelerin sayısı
    selected_count = len(selected_articles)
    
    # Tavsiye edilen makalelerin sayısı
    recommended_count = top_n
    
    # Doğru önerilen makalelerin sayısı
    correct_count = sum(1 for article in recommended_articles[:top_n] if article in selected_articles)
    
    # Precision hesapla
    precision = correct_count / recommended_count if recommended_count > 0 else 0
    
    # Recall hesapla
    recall = correct_count / selected_count if selected_count > 0 else 0
    
    return precision, recall

# Kullanıcı tarafından seçilen makalelerin isimleri
selected_articles = ["a", "b"]

# Önerilen makalelerin isimleri
recommended_articles = ["z", "x", "a", "c", "b"]

# Precision ve recall hesapla
precision, recall = calculate_precision_recall(selected_articles, recommended_articles)
print("Precision:", precision)
print("Recall:", recall)
