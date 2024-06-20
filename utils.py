import pandas as pd
from sklearn.decomposition import PCA

def preprocess_data(videos):
    videos['publishedAt'] = pd.to_datetime(videos['publishedAt'])
    videos['month'] = videos['publishedAt'].dt.month
    videos['weekday'] = videos['publishedAt'].dt.weekday + 1
    videos['hour'] = videos['publishedAt'].dt.hour
    #videos = videos.drop(columns=['id', 'titlewordcount', 'descriptionwordcount', 'videoId', 'includestitleemoji', 'title', 'thumbnail', 'description', 'channel', 'publishedAt', 'tags', 'topicCategories', 'language', 'query', 'createdat', 'updatedat', 'categoryid', 'caption', 'publishedattime', 'publishedatday', 'likesperviewrate', 'commentsperviewrate'])
    videos = videos.fillna(videos.mean())
    return videos

def preprocess_input(input):
    input['titlecharlength'] = input['title'].apply(len)
    input['descriptioncharlength'] = input['description'].apply(len)
    input = input.drop(columns=['title', 'description'])
    new_order = ['duration', 'titlecharlength', 'descriptioncharlength', 'month', 'weekday', 'hour', 'totalChannelViews', 'subscriberCount', 'videoCount']
    input = input[new_order]
    return input


def remove_outliers(df, columns): # Funktion von Chat GPT
    for col in columns: 
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df
