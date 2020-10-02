FROM ubuntu:latest
RUN apt-get update

# Sets the timezone to mountain daylight time
RUN export DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/America/Denver /etc/localtime
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Install cron and script dependencies
RUN apt-get install -y cron poppler-utils curl

# Add necessary files into system
ADD crontab /etc/cron.d/simple-cron
ADD script.sh /script.sh
RUN chmod 0744 /script.sh

# Give execution rights on the cron job
# Create the log file to be able to run tail
RUN chmod 0644 /etc/cron.d/simple-cron

# Run the command on container startup
RUN touch /var/log/cron.log
CMD ["cron", "-f"]
