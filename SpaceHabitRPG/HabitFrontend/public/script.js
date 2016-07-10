$(function () {
    localDate = new Date()
    $.ajax({
        url: "main/checkin",
        type: 'get',
        dataType: 'json',
        data: { 'utcElapsedTime': Date.now(), 'utcOffset': localDate.getTimezoneOffset() },
        success: onCheckInSuccess
    });
});

function onCheckInSuccess(data) {
    console.log(data);
}

//$(function(){
    
    //$.ajax({
    //    url: "/hero",
    //    type: 'get',
    //    dataType: 'json',
    //    error: function (p1,p2,p3) {
    //        //alert(p3);
    //    },
    //    success: function (data) {
    //        //heroFromJson = JSON.parse(data);
            

    //        //ko.applyBindings(new SpaceHabitModel(heroFromJson));
    //    }
    //});
  
//  function clearDailyEditInputs(){
//    $('#edit_daily_box input').val("");
//    $('#edit_daily_box textarea').val("");
//    $('#daily_urgency .selected_danger_radio').removeClass("selected_danger_radio");
//    $('#daily_urgency .danger_radio:nth-of-type(4)').addClass("selected_danger_radio");
//    $('#daily_difficulty .selected_danger_radio').removeClass("selected_danger_radio");
//    $('#daily_difficulty .danger_radio:nth-of-type(4)').addClass("selected_danger_radio");
//    $('#daily_rate input').val("1");
//    $('.day_check').prop('checked','true');
    
//  }
  
//  function clearHabitEditInputs(){
	  
//  }
  
//  function clearTodoEditInputs(){}
  
//  function clearGoodsEditInputs(){}

  
//  var SpaceHabitModel = function(heroModel){
    
//    var self = this;
    
//    self.hero = {'name': ko.observable(heroModel.name),
//      'lvl': ko.observable(heroModel.lvl),
//      'gold': ko.observable(heroModel.gold),
//      'maxHp':ko.observable(heroModel.maxHp),
//      'nowHp': ko.observable(heroModel.nowHp),
//      'maxXp': ko.observable(heroModel.maxHp),
//      'nowXp': ko.observable(heroModel.nowXp),
//    };

//    //self.dailies = ko.observableArray(GetDailies());
//    //self.finishedDailies = ko.observableArray(GetFinishedDailies());
//    //self.habits = ko.observableArray(GetHabits());
//    //self.todos = ko.observableArray(GetTodos());
//    //self.IRLGoods = ko.observableArray(GetIRLPrizes());
//    //self.disposableGoods = ko.observableArray(GetDisposableGoods());
//    //self.armsGoods = ko.observableArray(GetArmsPrizes());
//	//self.items = ko.observableArray(GetDisposableGoods());
    
//    self.doDaily = function(daily){
//    };
//    self.undoDaily = function(daily){};
//    self.dohabit = function(habit){};
//    self.doTodo = function(todo){};
//    self.buyGood = function(good){};
//	self.useItem = function(item){};

    
//    self.getHeroHealthPercent = function(){
//      var percent = Math.round((self.hero.nowHp()/self.hero.maxHp())*100);
//      return percent +"%";
//    };
    
//    self.getHeroXpPercent = function(){
//      var percent = Math.round((self.hero.nowXp()/self.hero.maxXp())*100);
//      return percent + "%";
//    };
    
//    self.getMonsterHealthPercent = function(){
//        //var percent = Math.round((self.monster.nowHp()/self.monster.maxHp())*100);
//        percent = 75;
//      return percent + "%";
//    };
    
//    self.getDaysUntilTodoEnds = function(todo){
//      return todo.dueDate;
//    };
    
//    self.getDaysUntilTodoStarts = function(todo){
//      return todo.effectiveDate;
//    };
    
//    self.getDaysUntilDailyEnds = function(daily){
//      return daily.daysLeft;
//    };
    
//  };
  
  
  
  
//  $('button[name="open_add_daily"]').click(function(){
//    clearDailyEditInputs();
//    $('#edit_daily_box').modal('show');
//  });
  
//  $('button[name="open_add_habit"]').click(function(){
//    clearHabitEditInputs();
//    $('#edit_habit_box').modal('show');
//  });
  
//  $('button[name="open_add_todo"]').click(function(){
//    clearTodoEditInputs();
//    $('#edit_todo_box').modal('show');
//  });
  
//  $(".task_open_extra_options").click(function(){
	  
//  });
  
//   $('.danger_radio:nth-of-type(4)').addClass("selected_danger_radio");
   
//   $('.danger_radio').click(function(){
//     $(this).siblings('.selected_danger_radio').removeClass("selected_danger_radio");
//     $(this).addClass("selected_danger_radio");
//   });
   
//});