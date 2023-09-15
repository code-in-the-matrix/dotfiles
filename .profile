JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# Apache maven
MAVEN_HOME="/home/swayam/applications/apache-maven-3.9.1"

#Add
PATH="$PATH:/usr/local/bin:/usr/bin:/bin"
PATH="$PATH:$HOME/.local/bin"
PATH="$PATH:$HOME/.config/emacs/bin"


# Flutter path
PATH="$PATH:/home/swayam/applications/flutter/bin"


PATH="$PATH:$MAVEN_HOME/bin"


# Added by Toolbox App
PATH="$PATH:/home/swayam/.local/share/JetBrains/Toolbox/scripts"

PATH="$PATH:/home/swayam/.pub-cache/bin"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/swayam/applications/google-cloud-sdk/path.bash.inc' ]; then . '/home/swayam/applications/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/swayam/applications/google-cloud-sdk/completion.bash.inc' ]; then . '/home/swayam/applications/google-cloud-sdk/completion.bash.inc'; fi

