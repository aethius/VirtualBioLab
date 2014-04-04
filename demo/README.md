//Make sure this is saved as "local.js" in /demo/config/locales/

port: process.env.PORT || 1337,

environment: process.env.NODE_ENV || 'development',

  adapters: {

    'default': 'mongo',

    mongo: {
      module    : 'sails-mongo',
      host      : 'localhost',
      user      : '',
      password  : '',
      database  : 'VirtualBiologyLab',

      schema    : true
    }
  }

};