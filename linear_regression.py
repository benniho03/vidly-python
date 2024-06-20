from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from utils import preprocess_data, preprocess_input, remove_outliers

def linear_regression(videos, input):
    videos = preprocess_data(videos)
    input = preprocess_input(input)
    
    videos = remove_outliers(videos, ['duration', 'titlecharlength', 'descriptioncharlength', 'month', 'weekday', 'hour', 'viewCount', 'commentCount', 'likeCount'])

    # Wenn man versucht, mit diesen Angaben den viewCount direkt zu berechnen, kommt ein R2-Score von > 0.1 raus. Daher werden zur Unterstützung erst die Likes und Comments berechnet.
    # Am Ende ist das Ergebnis trotzdem nicht gut (nur 0.34), jedoch deutlich besser als ohne likes und comments

    # likeCount mit sehr wenig Anhaltspunkte berechnen

    X = videos[['duration', 'titlecharlength', 'descriptioncharlength', 'month', 'weekday', 'hour']]
    y = videos['likeCount']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2_likes = r2_score(y_test, y_pred)        
    predictedLikes = model.predict(input)
    input['likeCount'] = predictedLikes[0]
    
    # commentCount berechnen, berechneter likeCount ist mit drin
    X = videos[['duration', 'titlecharlength', 'descriptioncharlength', 'month', 'weekday', 'hour', 'likeCount']]
    y = videos['commentCount']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2_comments = r2_score(y_test, y_pred)        
    predictedComments = model.predict(input)
    input['commentCount'] = predictedComments[0]

    # viewCount berechnen, nimmt berechneten likeCount und commenCount mit rein
    X = videos[['duration', 'titlecharlength', 'descriptioncharlength', 'month', 'weekday', 'hour', 'likeCount', 'commentCount']]
    y = videos['viewCount']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2_views = r2_score(y_test, y_pred)        
    predictedViews= model.predict(input)


    print("-- Lineare Regression --") 
    print(f"Predicted Likes: {predictedLikes[0]} | R2-Score: {r2_likes}")
    print(f"Predicted Comments: {predictedComments[0]} | R2-Score: {r2_comments}")
    print(f"Predicted Views: {predictedViews[0]} | R2-Score: {r2_views}")
    

