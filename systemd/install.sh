#!/bin/bash

SERVICE_NAME=sort_images

cp $SERVICE_NAME.service /etc/systemd/system/$SERVICE_NAME.service
cp $SERVICE_NAME.timer /etc/systemd/system/$SERVICE_NAME.timer

systemctl daemon-reload
systemctl enable $SERVICE_NAME.timer

