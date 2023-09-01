#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
  phoneNumber: '08166164984',
  message: 'Job Opening Available',
});

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
