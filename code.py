from deep_translator import GoogleTranslator

file_path = 'messages.php'
translated_file_path = 'messages_fr.php'

# Reading the file content
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.readlines()
    
# Function to translate the values from English to French in the PHP key-value pairs

def translate_php_array(content, limit=100):
    translated_content = []
    count = 0
    translator = GoogleTranslator(source='en', target='fr')

    for line in content:
        if "=>" in line and count < limit:
            key, value = line.split("=>")
            value = value.strip().strip(",").strip("'").strip()  # Cleaning the value

            # Translate the value
            translated_value = translator.translate(value)

            # Escape apostrophes in the translated value
            print(translated_value)
            if translated_value is not None:
              translated_value = translated_value.replace("'", "\\'")
              # Rebuild the line with the translated value
              translated_line = f"{key} => '{translated_value}',\n"
              translated_content.append(translated_line)
            else:
              translated_content.append(line)
              print("ligne non traduite: ",line)
            count += 1
        else:
            translated_content.append(line)

    return translated_content

# Translating the first 100 lines
translated_lines = translate_php_array(file_content, limit=100)


# Saving the manually translated content into a new file
with open(translated_file_path, 'w', encoding='utf-8') as file:
    file.writelines(translated_lines)
