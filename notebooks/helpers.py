


def read_data(file_path):
    tokens = []
    tags = []
    
    tweet_tokens = []
    tweet_tags = []
    for line in open(file_path, encoding='utf-8'):
        line = line.strip()
        if not line:
            if tweet_tokens:
                tokens.append(tweet_tokens)
                tags.append(tweet_tags)
            tweet_tokens = []
            tweet_tags = []
        else:
            token, tag = line.split()
            # Replace all urls with <URL> token
            # Replace all users with <USR> token

            if token.find('http://') == 0 or token.find('https://') == 0:
                token = '<URL>'
            if token[0] == '@':
                token = '<USR>'
                       
            tweet_tokens.append(token)
            tweet_tags.append(tag)
            
    return tokens, tags