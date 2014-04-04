/**
 * UserController
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

module.exports = {
    
    //sign-up page --> new.ejs
  'new': function (req, res) {
  	res.view();
  },

  create: function (req,res,next) {
	//create a user with the params sent from the sign-up form --> new.ejs
	User.create( req.params.all(), function userCreated (err, user) {

		//if ther's an error
		if (err) {
			//console.log(err);
			req.session.flash= {
				err: err
			}



			//returns user back to sign-up page
			return res.redirect('/user/new');
		}

		//Log User In
		req.session.authenticated = true;
		req.session.User = user;
		
		//after successfully creating the user
		//redirect to the show action
		
		res.redirect('/user/show/'+user.id);
	});
  },

  // render the profile view (/views/show.ejs)
  show: function (req, res, next) {
  	User.findOne(req.param('id'), function foundUser (err,user) {
  		if (err) return next(err);
  		if (!user) return next();
  		res.view({
  			user: user
  		});
  	});
  },

  index: function (req, res, next) {

  	

  	//array of all users
  	User.find(function foundUsers (err, users) {
  		if (err) return next(err);
  		// pass array down to /views/index.ejs page
  		res.view({
  			users: users
  		});
  	});
  },

  //render edit view (/views/edit.ejs)
  edit: function (req, res, next) {

  	//Find user from the id passed in via params
  	User.findOne(req.param('id'), function foundUser (err, user) {
  		if (err) return next(err);
  		if(!user) return next('User doesn\'t exist.');

  		res.view({
  			user: user
  		});
  	});
  },

  //process info from edit view
  update: function (req, res, next) {
  	User.update(req.param('id'), req.params.all(), function userUpdated (err) {
  		if (err) {
  			return res.redirect('/user/edit/' + req.param('id'));
  		}

  		res.redirect('/user/show/' + req.param('id'));
  	});
  },

  //deletes user from database
  destroy: function (req, res, next) {

  	User.findOne(req.param('id'), function foundUser (err, user) {
  		if (err) return next(err);

  		if (!user) return next('User doesn\'t exist.');

  		User.destroy(req.param('id'), function userDestroyed(err) {
  			if (err) return next(err);

  		});

  		res.redirect('/user');
  	});
  }
  
};
