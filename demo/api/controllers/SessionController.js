/**
 * ControllerController
 *
 * @module      :: Controller
 * @description	:: A set of functions called `actions`.
 *
 *                 Actions contain code telling Sails how to respond to a certain type of request.
 *                 (i.e. do stuff, then send some JSON, show an HTML page, or redirect to another URL)
 *
 *                 You can configure the blueprint URLs which trigger these actions (`config/controllers.js`)
 *                 and/or override them with custom routes (`config/routes.js`)
 *
 *                 NOTE: The code you write here supports both HTTP and Socket.io automatically.
 *
 * @docs        :: http://sailsjs.org/#!documentation/controllers
 */

 var bcrypt = require('bcrypt');

module.exports = {
    
  'new': function(req, res) {

    
    res.view('session/new');
  },

  create: function(req, res, next) {

    //Checks for email and password in params 
    //if no inputs, redirect back with error message
    if (!req.param('email') || !req.param('password')) {

      var usernamePasswordRequiredError = [{name: 'usernamePasswordRequired', message: 'You must enter an email address and password.'}]
      req.session.flash = {
        err: usernamePasswordRequiredError
      }

      res.redirect('/session/new');
      return;
    }

    //Find user through email
    User.findOneByEmail(req.param('email')).done(function(err, user) {
      if (err) return next(err);

      //If no user found
      if (!user) {
        var noAccountError = [{name: 'noAccount', message: 'The email address ' + req.param('email') + ' not found.'}]
        req.session.flash = {
          err: noAccountError
        }
        res.redirect('/session/new');
        return;
      }
    
    //Compare password from params to encrypted password of found user
    bcrypt.compare(req.param('password'), user.encryptedPassword, function(err, valid) {
      if (err) return next(err);

      //If password doesn't match
      if(!valid) {
        var usernamePasswordMismatchError = [{name: 'usernamePasswordMismatch', message: 'Invalid password.'}]
        req.session.flash = {
          err: usernamePasswordMismatchError
        }
        res.redirect('/session/new');
        return;
      }

      //Log in user
      req.session.authenticated = true;
      req.session.User = user;

      //Redirect to user's profile page (/views/user/show.ejs)
      res.redirect('/user/show/' + user.id);
    });
  });

  }


  /**
   * Overrides for the settings in `config/controllers.js`
   * (specific to ControllerController)
   */
  
  
};
