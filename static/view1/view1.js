'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ["$scope", "$http", "$timeout", function($scope, $http, $timeout) {
     $scope.at_least_one_question_loaded = false;
     $scope.answer_choice = {};
     $scope.alert_message = "";
     $scope.alert_additional_details = [];
     $scope.is_loading = false;
     $scope.staging = false;
     $scope.show_log = false;
     $scope.question_tests = [];

     $scope.all_question_statuses = []

     $http.get("/resource_count").then(function(response){
            $scope.resource_count = response.data;
            console.log("Resource Count = " + $scope.resource_count);
        }, function(response){
            console.error(response)
        })

}]);