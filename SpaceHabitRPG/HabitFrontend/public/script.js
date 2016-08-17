$(function () {
    var localDate = new Date()
    var noticeData = null;
    var preventPopUps = false;
    var gu = new HabitUtilities();
    var selectedChoiceIndex = -1;

    $("button[name='story_intro_ok']").click(introCloseClick);
    $("button[name='zone_notice_ok']").click(zoneCloseClick);
    $("button[name='zone_choice_back']").click(zoneChoiceGoBackClick);
    $("button[name='zone_choice_ok']").click(zoneChoiceConfirm);
    $("#zone_choice_no_popups_check").click(blockPopupCheckForZoneChoiceClick);

    $("#story_notices").on('hidden.bs.modal', onStoryIntroHide);
    $("#zone_notices").on('hidden.bs.modal', onIntroZoneHide);

    $.ajax({
        url: "main/checkin",
        type: 'get',
        dataType: 'json',
        data: { 'utcElapsedTime': Date.now(), 'utcOffset': localDate.getTimezoneOffset() },
        success: onCheckInSuccess
    });

    function onStoryIntroHide() {
        /*
            this is called when the into message is closed and the user has 
            chosen to continue allowing pop-ups.
        */
        if (preventPopUps) {
            return;
        }
        $("#zone_notice_content").html(noticeData['zoneNotice']);
        $('#zone_notices').modal('show');
    }

    function onCheckInSuccess(data) {
        /*
            this should be called whenever the paige loads.
        */
        noticeData = data;
        $("#story_notice_content").html(data['storyNotice']);
        $('#story_notices').modal('show');
    }

    function onRegisterZoneSuccess() {
            
    }

    function onIntroZoneHide() {
        /*
            this is called when the home zone description box is closed by the
            user.
        */
        var zones = noticeData['zonePrompt'];
        if (preventPopUps) {
            var item = gu.arrayRandomChoice(zones);
            //JPTODO: send info to sever
            return;
        }
        ko.applyBindings(new zoneViewModel(zones), document.getElementById("zone_choices"));
        $('#zone_choices').modal('show');
    }

    function generalAjaxSuccess() {
        /*
            mostly for testing purposes
        */
        console.log("success");
    }

    function introCloseClick() {
        /*
            when the user clicks on the next button for the intro message
        */
        checkPreventPopupsCheckbox();
        $('#story_notices').modal('hide');
    }

    function zoneCloseClick() {
        /*
            when the user clicks on the next button for the home zone description box
        */
        checkPreventPopupsCheckbox();
        $('#zone_notices').modal('hide');
    }

    function zoneChoiceGoBackClick() {
        /*
            when the user clicks on the go back button after the user has selected a zone.
        */
        selectedZone = null;
        $("#picked_zone_description").addClass("hidden");
        $("#zone_choice_list").removeClass("hidden");
        $("button[name='zone_choice_back']").addClass("hidden");
        $("button[name='zone_choice_ok']").addClass("hidden");
    }

    function zoneChoiceConfirm(){
        /*
            when the user clicks OK after a zone has been selected or if 
            the user clicks OK after the block pop-ups checkbox has been
            marked.
        */
        checkPreventPopupsCheckbox();
        $('#zone_choices').modal('hide');
        if (selectedChoiceIndex > -1) {

            $.ajax({
                url: "main/register_zone",
                type: 'get',
                dataType: 'json',
                data: { 'selectedZoneIndex': selectedChoiceIndex },
                success: onRegisterZoneSuccess
            });
        }
        else {
            var zones = noticeData['zonePrompt'];
            var item = gu.arrayRandomChoice(zones);
            //JPTODO: send info to sever
            return;
            
        }

        
    }

    function blockPopupCheckForZoneChoiceClick() {
        /*
            if the user checks the no pop-up checkbox on the zone selection
            window.
        */
        preventPopUps = $('#zone_choice_no_popups_check').prop('checked');
        console.log("check checked");
        if (preventPopUps) {
            $("button[name='zone_choice_ok']").removeClass("hidden");
        }
        else {
            if ($("#picked_zone_description").hasClass("hidden")) {
                $("button[name='zone_choice_ok']").addClass("hidden");
            }
        }
    }

    function checkPreventPopupsCheckbox() {
        /*
            this should be called on most next screen clicks on the opening
            box. This sends a message to the server to not send anymore 
            pop-ups for this user.
        */
        preventPopUps = $('#no_popups_check').prop('checked') ||
            $('#zone_choice_no_popups_check').prop('checked');
        if (preventPopUps) {
            $.ajax({
                url: "main/disable_popups",
                type: "get",
                success: generalAjaxSuccess
            });
        }
    }

    function zoneChoice(zoneItem) {
        /*
            js class to be a knockout.js zone item.
            args should be fed from noticeData object
            args:
                zoneItem:
        */
        var self = this;
        self.name = zoneItem['fullName'];
        self.lvl = zoneItem['lvl'];
        self.description = zoneItem['description'];
    }

    function zoneViewModel(zoneList) {
        /*
            knockout.js
            args:
                zoneList:
                    pass value for 'zonePrompt' from the global noticeData
        */
        var self = this;
        var transformedZoneList = [];
        for (var i = 0; i < zoneList.length; i++) {
            transformedZoneList.push(new zoneChoice(zoneList[i]));
        }

        self.onZoneChoiceClick = function (index,choice,e) {
            /*
                when the user clicks on any of the opening zone choices.
            */
            selectedChoiceIndex = index;
            $("#zone_choice_list").addClass("hidden");
            var $zoneDesc = $("#picked_zone_description")
            $zoneDesc.html("");
            $zoneDesc.removeClass("hidden");
            $zoneDesc.html(choice.description);
            $("button[name='zone_choice_back']").removeClass("hidden");
            $("button[name='zone_choice_ok']").removeClass("hidden");
        }

        self.choices = ko.observableArray(transformedZoneList);
    }

});



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