db = db.getSiblingDB('smarthire');
db.createCollection('jobs');
db.jobs.insertMany([
  {
    title: 'Frontend Developer',
    company: 'SmartTech',
    location: 'Remote',
    salary: '$70k - $90k',
    description: 'Build React applications.'
  }
]);
