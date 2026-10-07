"""Complete consulting-section and footer-introduction localization.

Product translations are owned by their existing source modules.
"""

DATA = {'en': {'consulting_eyebrow': 'Consulting services',
        'consulting_heading': 'Airport consulting',
        'consulting_intro': 'Planning, simulation and technical support for airports and engineering teams.',
        'consulting_projects_heading': 'Project applications',
        'consulting_tab_overall': 'Overall',
        'consulting_tabs_aria': 'Consulting service areas',
        'consulting_overall_intro': 'Typical projects include new airports and terminals, expansion, refurbishment during live operations, '
                                    'airline or facility relocation, phased investment and operational improvement.',
        'consulting_overall_01_title': 'Airline relocation',
        'consulting_overall_01_role': 'Assess whether check-in, security and transfer facilities can accommodate relocated airlines, and '
                                      'compare suitable layouts.',
        'consulting_overall_02_title': 'New terminals and airport expansion',
        'consulting_overall_02_role': 'Compare opening dates, facility size and the division of functions between new and existing '
                                      'terminals.',
        'consulting_overall_03_title': 'Airside layout changes',
        'consulting_overall_03_role': 'Assess how revised taxiways and stands affect aircraft movements and ground-handling vehicle flows.',
        'consulting_overall_04_title': 'Refurbishment during live operations',
        'consulting_overall_04_role': 'Assess which facilities can close together and compare temporary routes and construction sequences.',
        'consulting_overall_05_title': 'Joint design and engineering proposals',
        'consulting_overall_05_role': 'Join proposals as a technical partner for simulation and capacity assessment, then undertake the '
                                      'agreed analysis after award.',
        'consulting_overall_06_title': 'Airport development strategy',
        'consulting_overall_06_role': 'Assess demand, capacity and alternatives to support investment timing and facility sizing.',
        'consulting_tab_demand': 'Demand & Schedules',
        'consulting_demand_intro': 'Translate future demand into operating scenarios, facility requirements and expansion decisions.',
        'consulting_task_01_title': 'Future traffic and passenger demand',
        'consulting_task_01_description': 'Develop target-year and growth-stage scenarios from existing forecasts and operating data to '
                                          'assess facility and operating requirements.',
        'consulting_task_02_title': 'Design-day and peak-hour demand',
        'consulting_task_02_description': 'Translate annual demand into representative-day, peak-day and hourly profiles to establish the '
                                          'loads facilities must accommodate.',
        'consulting_task_03_title': 'Future flight schedule generation',
        'consulting_task_03_description': 'Develop design-day schedules from demand, fleet mix, airline patterns and operating hours, then '
                                          'assess their operational feasibility.',
        'consulting_task_04_title': 'Fleet mix and airline patterns',
        'consulting_task_04_description': 'Compare how aircraft size, airline and route mix, and arrival and departure banks affect gate, '
                                          'stand and terminal demand.',
        'consulting_task_05_title': 'Passenger segments and arrival profiles',
        'consulting_task_05_description': 'Model when and where departing, arriving and transfer passengers reach facilities, accounting '
                                          'for show-up patterns and gate allocations.',
        'consulting_task_06_title': 'Capacity gaps and expansion triggers',
        'consulting_task_06_description': 'Test rising demand against capacity limits and remaining headroom to recommend expansion '
                                          'thresholds, indicative timing and facility priorities.',
        'consulting_tab_terminal': 'Terminal & Landside',
        'consulting_terminal_intro': 'Assess passenger processing, facility layouts, airline relocation, construction phasing and access '
                                     'arrangements.',
        'consulting_task_07_title': 'Terminal facility sizing and adequacy',
        'consulting_task_07_description': 'Assess processing facilities and waiting areas against demand and service criteria to identify '
                                          'required facility quantities and operating hours.',
        'consulting_task_08_title': 'Departure processes and operating plans',
        'consulting_task_08_description': 'Compare facility opening, operating hours and staffing across check-in, self bag drop, '
                                          'boarding-pass checks, security and departure immigration.',
        'consulting_task_09_title': 'Arrivals, baggage reclaim and customs',
        'consulting_task_09_description': 'Model arrival immigration, baggage reclaim and customs together to assess how changes at one '
                                          'stage affect total processing time and downstream congestion.',
        'consulting_task_10_title': 'Transfer flows and terminal connections',
        'consulting_task_10_description': 'Assess transfer security, gate-to-gate movement, corridors and inter-terminal transit platforms '
                                          'for congestion and connection times.',
        'consulting_task_11_title': 'Airline relocation and facility impacts',
        'consulting_task_11_description': 'Compare airline moves between terminals, concourses, check-in zones or gates for passenger '
                                          'distribution, facility loads, transfer routes and gate lounge congestion.',
        'consulting_task_12_title': 'New terminals and phased expansion',
        'consulting_task_12_description': 'Compare facility size, layout, roles and connections with existing terminals to assess capacity '
                                          'at opening and later expansion stages.',
        'consulting_task_13_title': 'Refurbishment during live airport operations',
        'consulting_task_13_description': 'Assess closures and reduced facility availability to determine workable closure combinations '
                                          'and temporary operating arrangements.',
        'consulting_task_14_title': 'Passenger circulation and queue layouts',
        'consulting_task_14_description': 'Compare corridor widths, partitions, diversions and queue layouts for walking distance, '
                                          'congestion and dwell time, then recommend spatial improvements.',
        'consulting_task_15_title': 'Landside access and transport interfaces',
        'consulting_task_15_description': 'Assess passenger and vehicle arrivals and layout options for terminal curbs, parking, access '
                                          'roads and public transport interfaces within the agreed scope.',
        'consulting_task_16_title': 'Combined conditions and stress scenarios',
        'consulting_task_16_description': 'Combine peak demand, flight delays, closures and airline relocation to identify vulnerable '
                                          'areas and compare congestion relief and recovery options.',
        'consulting_tab_airside': 'Airside',
        'consulting_airside_intro': 'Evaluate runway, taxiway, stand and support-facility plans alongside aircraft and ground-handling '
                                    'operations.',
        'consulting_task_17_title': 'Runway capacity and flight delays',
        'consulting_task_17_description': 'Model operating modes, occupancy, separation and concentrated traffic to assess runway '
                                          'throughput and arrival and departure delays, including low-visibility conditions.',
        'consulting_task_18_title': 'Rapid-exit taxiway locations and layouts',
        'consulting_task_18_description': 'Compare rapid-exit taxiway positions and spacing using aircraft landing characteristics and '
                                          'runway occupancy considerations.',
        'consulting_task_19_title': 'Airside layout changes and impacts',
        'consulting_task_19_description': 'Assess how new, extended, reconnected or closed runways, taxiways and aprons affect routes, '
                                          'taxi times, bottlenecks and operational interference.',
        'consulting_task_20_title': 'Stand allocation and simultaneous pushback',
        'consulting_task_20_description': 'Assess aircraft compatibility, contact and remote stand allocation, occupancy and simultaneous '
                                          'movements to recommend layout and operating alternatives.',
        'consulting_task_21_title': 'Aircraft and ground-handling vehicle movements',
        'consulting_task_21_description': 'Model aircraft movement and pushback alongside vehicle tasks and routes to assess service-road '
                                          'congestion, crossing interference and vehicle operating plans.',
        'consulting_task_22_title': 'Cargo aprons and freighter operations',
        'consulting_task_22_description': 'Assess large-freighter stand compatibility, occupancy, access routes and connections with cargo '
                                          'terminals and ground logistics.',
        'consulting_task_23_title': 'MRO, hangar and GA/FBO access',
        'consulting_task_23_description': 'Review aircraft compatibility, hangar access, towing routes and interactions with adjacent '
                                          'aprons and service roads.',
        'consulting_task_24_title': 'De-icing facility layouts and operations',
        'consulting_task_24_description': 'Assess simultaneous accommodation, access and exit routes, and aircraft clearances, then '
                                          'compare queues and departure delays under variable processing times.',
        'consulting_task_25_title': 'ARFF, fuel and support-facility siting',
        'consulting_task_25_description': 'Assess rescue and firefighting, fuel and utility facility locations, access routes and service '
                                          'coverage to support layout and operating decisions.',
        'consulting_task_26_title': 'Tower visibility and obstacle constraints',
        'consulting_task_26_description': 'Compare sightlines and blind spots, and review obstacle limitation surface overlaps associated '
                                          'with runway and surrounding facility plans at the planning stage.',
        'consulting_tab_digital': 'Digital Twins',
        'consulting_digital_intro': 'Model airport development stages, validate operating rules and build the analysis capabilities '
                                    'required for the project.',
        'consulting_task_27_title': 'Current and future airport models',
        'consulting_task_27_description': 'Prepare spatial inputs and model existing, opening, interim expansion and ultimate layouts with '
                                          'the facilities planned for each stage.',
        'consulting_task_28_title': 'Airport-specific models and operational validation',
        'consulting_task_28_description': 'Configure distinctive layouts, facility-use rules and operating procedures, then validate and '
                                          'calibrate against available observations and operating records.',
        'consulting_task_29_title': 'Design overlays and spatial rendering',
        'consulting_task_29_description': 'Compare existing plans, alternatives and construction phases, and explain aircraft, vehicle and '
                                          'passenger flows through plan views, spatial models and simulation videos.',
        'consulting_task_30_title': 'Custom KPIs and analysis features',
        'consulting_task_30_description': 'Define airport-specific measures, including simultaneous gate operations and transfer-time '
                                          'exceedances, and configure the required data inputs, outputs and result-access functions.',
        'consulting_scope_note': 'Scope, model detail and assessment criteria are agreed against your airport data, operating conditions '
                                 'and project requirements. Additional studies, feature development and external-system integration are '
                                 'scoped with the required schedule.',
        'consulting_expertise_heading': 'Technology and airport experience',
        'consulting_expertise_origin': 'Team Flexa grew out of Incheon International Airport Corporation’s in-house venture programme. Our '
                                       'team has worked on operations improvement and expansion at Incheon Airport, as well as assignments '
                                       'within the corporation’s overseas airport business.',
        'consulting_expertise_01_title': 'In-house software',
        'consulting_expertise_01_description': 'We develop and own our software, adapting models and functions to the study while reducing '
                                               'the need for separate analysis tools or specialist staff.',
        'consulting_expertise_02_title': 'Custom KPIs and analysis features',
        'consulting_expertise_02_description': 'We use your performance measures, assessment criteria and reporting formats, agreeing '
                                               'additional development or integration where existing functions are insufficient.',
        'consulting_expertise_03_title': 'Airport-specific rules and layouts',
        'consulting_expertise_03_description': 'We model terminal connections, airline facility-use rules, stand configurations, '
                                               'ground-handling routes and time-dependent restrictions.',
        'consulting_expertise_04_title': 'Existing data and models',
        'consulting_expertise_04_description': 'We use available airport, flight and facility data and existing models to reduce setup '
                                               'time, validating against your observations and agreed criteria.',
        'consulting_expertise_05_title': 'Linked aircraft, vehicle and passenger flows',
        'consulting_expertise_05_description': 'Aircraft movements and vehicle tasks are modelled together; gate allocations and passenger '
                                               'arrivals link airside and terminal studies to assess the wider effects of facility '
                                               'changes.',
        'consulting_engagements_heading': 'Working with us',
        'consulting_engagements_terms': 'Engagements are available as consulting only or consulting with selected software features or '
                                        'licences. Direct access to results or follow-on review functions, and their terms of use, are '
                                        'agreed separately.',
        'consulting_engagements_01_title': 'Project-based consulting',
        'consulting_engagements_01_application': 'Airport expansion, airline relocation, construction plans and other defined planning '
                                                 'needs.',
        'consulting_engagements_01_role': 'We develop models, compare options and recommend improvements, with findings prepared for '
                                          'planning and budget reviews.',
        'consulting_engagements_02_title': 'Joint proposals and project delivery',
        'consulting_engagements_02_application': 'Simulation and capacity assessment within design, engineering and consulting '
                                                 'assignments.',
        'consulting_engagements_02_role': 'At proposal stage, we agree the method, responsibilities, programme and fee; after award, we '
                                          'undertake the agreed analysis to test designs and compare alternatives.',
        'consulting_engagements_03_title': 'Ongoing technical partnership',
        'consulting_engagements_03_application': 'Specialist analysis across multiple airport projects.',
        'consulting_engagements_03_role': 'We provide design review, scenario analysis and technical advice over an agreed period, without '
                                          'requiring a dedicated in-house analysis team.',
        'consulting_deliverables_heading': 'Deliverables',
        'consulting_deliverables_usage_rights': 'Use rights and duration for supplied data, models, accounts or solution functions are '
                                                'defined for the engagement.',
        'consulting_deliverables_01_title': 'Consulting reports',
        'consulting_deliverables_01_use': 'Technical reports or executive summaries covering objectives, option assessments, '
                                          'recommendations and investment priorities.',
        'consulting_deliverables_02_title': 'HTML web reports',
        'consulting_deliverables_02_use': 'Browser-based review of scenarios, comparisons and spatial visualizations.',
        'consulting_deliverables_03_title': 'PDF and DOCX',
        'consulting_deliverables_03_use': 'Project submissions, internal review, collaborative editing and printed distribution.',
        'consulting_deliverables_04_title': 'Videos and rendered images',
        'consulting_deliverables_04_use': 'Simulation videos, alternative-layout comparisons and spatial renderings for meetings and '
                                          'stakeholder communication.',
        'consulting_deliverables_05_title': 'Data, models and selected solution components',
        'consulting_deliverables_05_use': 'Agreed datasets, model packages, access accounts or functions supplied for the engagement.',
        'consulting_programme_heading': 'Programme and fees',
        'consulting_programme_01_title': 'Project-based programme',
        'consulting_programme_01_description': 'We align the programme with your project schedule, allowing for study scope, data '
                                               'preparation, model validation and reviews.',
        'consulting_programme_02_title': 'Fixed-period support',
        'consulting_programme_02_description': 'Design review, scenario analysis and technical advice are available for agreed periods, '
                                               'such as one, three or six months; workload, frequency and response times are agreed '
                                               'separately.',
        'consulting_programme_03_title': 'Phased delivery',
        'consulting_programme_03_description': 'Commission studies at concept, preliminary design, detailed design and construction '
                                               'stages, with additional reviews as plans change.',
        'consulting_programme_04_title': 'Pricing',
        'consulting_programme_04_description': 'Fees reflect scope, project scale, duration, the number of alternatives and '
                                               'custom-development requirements.',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. All rights reserved.',
        'flexa_about_title': 'Who is Flexa',
        'flexa_about_p1': 'The Flexa brand is offered by TeamFlexa CO., LTD., a specialized airport solutions company that decodes the '
                          'complexity of airport operations through data, delivering optimal outcomes using simulation technologies and '
                          'AI-driven analytics. We go beyond analysis to provide actionable insights that drive real operational '
                          'improvements.',
        'flexa_about_p2': 'Originating as an in-house venture at Incheon International Airport, TeamFlexa leverages experience and data '
                          "from one of the world's leading airport environments. We deliver end-to-end consulting and solutions under the "
                          'Flexa brand, from terminal operations optimization to mid- and long-term infrastructure strategy, enabling '
                          'clients to define complex challenges quantitatively and make the most effective decisions.',
        'flexa_about_p3': 'Serving global airports, airport operators, and engineering & construction firms, TeamFlexa diagnoses problems '
                          'with speed and precision, designs tailored strategies, and ensures execution. We redefine the standards of '
                          'airport operations and act as a leading partner for data-driven decision-making in the global market.'},
 'ko': {'consulting_eyebrow': '컨설팅 서비스',
        'consulting_heading': '공항 컨설팅',
        'consulting_intro': '공항과 엔지니어링사를 위한 계획, 시뮬레이션 및 기술 지원.',
        'consulting_projects_heading': '프로젝트 적용 분야',
        'consulting_tab_overall': '전체',
        'consulting_tabs_aria': '컨설팅 서비스 분야',
        'consulting_overall_intro': '신공항·신규 터미널, 확장, 운영 중 리뉴얼, 항공사·시설 이전, 단계별 투자 및 운영 개선 프로젝트를 수행합니다.',
        'consulting_overall_01_title': '항공사 이전',
        'consulting_overall_01_role': '체크인·보안검색·환승 시설의 이전 항공사 수용 가능성을 평가하고 적합한 배치 대안을 비교합니다.',
        'consulting_overall_02_title': '신규 터미널 및 공항 확장',
        'consulting_overall_02_role': '개항 시기, 시설 규모, 신규·기존 터미널 간 기능 분담을 비교합니다.',
        'consulting_overall_03_title': '에어사이드 배치 변경',
        'consulting_overall_03_role': '유도로와 주기장 변경이 항공기 이동 및 지상조업 차량 흐름에 미치는 영향을 평가합니다.',
        'consulting_overall_04_title': '운영 중 리뉴얼',
        'consulting_overall_04_role': '동시에 폐쇄할 수 있는 시설을 평가하고 임시 동선과 공사 순서를 비교합니다.',
        'consulting_overall_05_title': '설계·엔지니어링 공동 제안',
        'consulting_overall_05_role': '시뮬레이션·처리용량 평가 기술 파트너로 제안에 참여하고 수주 후 합의된 분석을 수행합니다.',
        'consulting_overall_06_title': '공항 개발 전략',
        'consulting_overall_06_role': '수요, 처리용량 및 대안을 평가하여 투자 시기와 시설 규모 결정을 지원합니다.',
        'consulting_tab_demand': '수요·운항 스케줄',
        'consulting_demand_intro': '미래 수요를 운영 시나리오, 시설 요구량 및 확장 의사결정으로 연결합니다.',
        'consulting_task_01_title': '미래 항공교통·여객 수요',
        'consulting_task_01_description': '기존 예측과 운영자료로 목표연도·성장단계별 시나리오를 구성하고 시설 및 운영 요구사항을 평가합니다.',
        'consulting_task_02_title': '설계일·피크시간 수요',
        'consulting_task_02_description': '연간 수요를 대표일·첨두일·시간대별 분포로 변환하여 시설이 수용해야 할 부하를 산정합니다.',
        'consulting_task_03_title': '미래 운항 스케줄 생성',
        'consulting_task_03_description': '수요, 기종 구성, 항공사 패턴 및 운영시간으로 설계일 운항 스케줄을 만들고 운영 가능성을 평가합니다.',
        'consulting_task_04_title': '기종 구성·항공사 운영 패턴',
        'consulting_task_04_description': '항공기 크기, 항공사·노선 구성 및 출도착 집중시간 변화가 게이트·주기장·터미널 수요에 미치는 영향을 비교합니다.',
        'consulting_task_05_title': '여객 유형·도착 분포',
        'consulting_task_05_description': '공항 도착 패턴과 게이트 배정을 고려하여 출발·도착·환승 여객이 시설에 도달하는 시간과 위치를 모델링합니다.',
        'consulting_task_06_title': '용량 부족·확장 검토 시점',
        'consulting_task_06_description': '수요 증가에 따른 용량 한계와 여유를 검토하고 확장 검토 기준, 예상 시기 및 시설 우선순위를 제안합니다.',
        'consulting_tab_terminal': '터미널·랜드사이드',
        'consulting_terminal_intro': '여객 처리, 시설 배치, 항공사 이전, 단계별 공사 및 접근 계획을 평가합니다.',
        'consulting_task_07_title': '터미널 시설 규모·적정성',
        'consulting_task_07_description': '수요와 서비스 기준에 따라 처리시설·대기공간을 평가하고 필요한 시설 수량과 운영시간을 도출합니다.',
        'consulting_task_08_title': '출발 프로세스·시설 운영계획',
        'consulting_task_08_description': '체크인, 셀프백드롭, 탑승권 확인, 보안검색 및 출국심사의 시설 개방·운영시간·인력 대안을 비교합니다.',
        'consulting_task_09_title': '입국·수하물 수취·세관',
        'consulting_task_09_description': '입국심사부터 수하물 수취·세관까지 함께 모델링하여 각 단계의 변화가 전체 처리시간과 후속 시설 혼잡에 미치는 영향을 평가합니다.',
        'consulting_task_10_title': '환승 흐름·터미널 연결',
        'consulting_task_10_description': '환승 보안검색, 게이트 간 이동, 연결통로 및 터미널 간 교통 승강장의 혼잡과 연결시간을 평가합니다.',
        'consulting_task_11_title': '항공사 이전·시설 영향',
        'consulting_task_11_description': '터미널·탑승동·체크인 구역·게이트 간 항공사 이전에 따른 여객 분포, 시설 부하, 환승 동선 및 탑승대기실 혼잡을 비교합니다.',
        'consulting_task_12_title': '신규 터미널·단계별 확장',
        'consulting_task_12_description': '시설 규모·배치·역할 및 기존 터미널과의 연결을 비교하여 개항과 후속 확장 단계의 처리용량을 평가합니다.',
        'consulting_task_13_title': '공항 운영 중 리뉴얼',
        'consulting_task_13_description': '시설 폐쇄와 가용 시설 감소를 검토하여 실행 가능한 폐쇄 조합과 임시 운영방안을 도출합니다.',
        'consulting_task_14_title': '여객 동선·대기열 배치',
        'consulting_task_14_description': '통로 폭, 가설벽, 우회 동선 및 대기열 배치를 보행거리·혼잡·체류시간 기준으로 비교하고 공간 개선안을 제안합니다.',
        'consulting_task_15_title': '랜드사이드 접근·교통 연계',
        'consulting_task_15_description': '합의된 범위 내에서 여객·차량 도착과 터미널 승하차장, 주차장, 접근도로 및 대중교통 연계시설의 배치 대안을 평가합니다.',
        'consulting_task_16_title': '복합 조건·스트레스 시나리오',
        'consulting_task_16_description': '첨두 수요, 항공편 지연, 시설 폐쇄 및 항공사 이전을 조합하여 취약 구역을 찾고 혼잡 완화·회복 대안을 비교합니다.',
        'consulting_tab_airside': '에어사이드',
        'consulting_airside_intro': '활주로·유도로·주기장·지원시설 계획을 항공기 및 지상조업 운영과 함께 평가합니다.',
        'consulting_task_17_title': '활주로 용량·항공편 지연',
        'consulting_task_17_description': '운영방식, 점유시간, 분리간격 및 교통 집중을 모델링하여 저시정 조건을 포함한 활주로 처리량과 출도착 지연을 평가합니다.',
        'consulting_task_18_title': '고속탈출유도로 위치·배치',
        'consulting_task_18_description': '항공기 착륙 특성과 활주로 점유를 고려하여 고속탈출유도로의 위치와 간격을 비교합니다.',
        'consulting_task_19_title': '에어사이드 배치 변경·영향',
        'consulting_task_19_description': '활주로·유도로·계류장의 신설, 연장, 재연결 및 폐쇄가 이동 경로, 지상 이동시간, 병목 및 운영 간섭에 미치는 영향을 평가합니다.',
        'consulting_task_20_title': '주기장 배정·동시 푸시백',
        'consulting_task_20_description': '항공기 수용 적합성, 접현·원격 주기장 배정, 점유 및 동시 이동을 평가하여 배치·운영 대안을 제안합니다.',
        'consulting_task_21_title': '항공기·지상조업 차량 이동',
        'consulting_task_21_description': '항공기 이동·푸시백과 차량 작업·경로를 함께 모델링하여 조업도로 혼잡, 교차 간섭 및 차량 운영계획을 평가합니다.',
        'consulting_task_22_title': '화물 계류장·화물기 운영',
        'consulting_task_22_description': '대형 화물기 주기장 적합성, 점유, 접근 경로 및 화물터미널·지상 물류와의 연결을 평가합니다.',
        'consulting_task_23_title': 'MRO·격납고·GA/FBO 접근',
        'consulting_task_23_description': '항공기 적합성, 격납고 접근, 견인 경로 및 인접 계류장·조업도로와의 상호 영향을 검토합니다.',
        'consulting_task_24_title': '제방빙 시설 배치·운영',
        'consulting_task_24_description': '동시 수용, 진출입 경로 및 항공기 이격거리를 평가하고 처리시간 변화에 따른 대기열과 출발 지연을 비교합니다.',
        'consulting_task_25_title': '소방·급유·지원시설 입지',
        'consulting_task_25_description': '구조·소방, 급유 및 유틸리티 시설의 위치·접근 경로·서비스 범위를 평가하여 배치와 운영 결정을 지원합니다.',
        'consulting_task_26_title': '관제탑 시야·장애물 제한',
        'consulting_task_26_description': '계획 단계에서 시야와 사각지대를 비교하고 활주로·주변 시설 계획에 따른 장애물 제한표면의 중첩을 검토합니다.',
        'consulting_tab_digital': '디지털 트윈',
        'consulting_digital_intro': '공항 개발 단계를 모델링하고 운영규칙을 검증하며 프로젝트에 필요한 분석 기능을 구현합니다.',
        'consulting_task_27_title': '현재·미래 공항 모델',
        'consulting_task_27_description': '공간 입력자료를 준비하고 단계별 계획시설을 반영하여 현재·개항·중간 확장·최종 배치를 모델링합니다.',
        'consulting_task_28_title': '공항 맞춤 모델·운영 검증',
        'consulting_task_28_description': '공항 고유의 배치, 시설 이용규칙 및 운영절차를 구성하고 확보된 관측자료·운영기록으로 검증·보정합니다.',
        'consulting_task_29_title': '설계 중첩·공간 렌더링',
        'consulting_task_29_description': '기존 계획, 대안 및 공사 단계를 비교하고 평면도·공간 모델·시뮬레이션 영상으로 항공기·차량·여객 흐름을 설명합니다.',
        'consulting_task_30_title': '맞춤 KPI·분석 기능',
        'consulting_task_30_description': '동시 게이트 운영, 환승시간 초과 등 공항별 지표를 정의하고 필요한 데이터 입출력 및 결과 조회 기능을 구성합니다.',
        'consulting_scope_note': '과업 범위, 모델 상세도 및 평가 기준은 공항자료, 운영조건과 프로젝트 요구사항에 맞춰 합의합니다. 추가 검토, 기능 개발 및 외부 시스템 연계는 필요한 일정과 함께 범위를 정합니다.',
        'consulting_expertise_heading': '기술과 공항 경험',
        'consulting_expertise_origin': 'Team Flexa는 인천국제공항공사의 사내벤처 프로그램에서 출발했습니다. 인천공항 운영 개선·확장과 공사의 해외공항 사업 내 과업을 수행한 경험을 보유하고 있습니다.',
        'consulting_expertise_01_title': '자체 소프트웨어',
        'consulting_expertise_01_description': '직접 개발·보유한 소프트웨어의 모델과 기능을 과업에 맞게 조정하여 별도 분석도구 도입이나 전문인력 확보 부담을 줄입니다.',
        'consulting_expertise_02_title': '맞춤 KPI·분석 기능',
        'consulting_expertise_02_description': '고객의 성과지표, 평가 기준 및 보고 형식을 적용하고 기존 기능으로 부족한 부분은 추가 개발·연계 범위를 합의합니다.',
        'consulting_expertise_03_title': '공항별 운영규칙·배치',
        'consulting_expertise_03_description': '터미널 연결, 항공사 시설 이용규칙, 주기장 구성, 지상조업 경로 및 시간대별 제한을 모델링합니다.',
        'consulting_expertise_04_title': '기존 데이터·모델 활용',
        'consulting_expertise_04_description': '확보된 공항·운항·시설자료와 기존 모델로 구축시간을 줄이고 고객의 관측자료와 합의된 기준에 따라 검증합니다.',
        'consulting_expertise_05_title': '항공기·차량·여객 흐름 연계',
        'consulting_expertise_05_description': '항공기 이동과 차량 작업을 함께 모델링하고 게이트 배정·여객 도착으로 에어사이드와 터미널 검토를 연결하여 시설 변경의 전체 영향을 평가합니다.',
        'consulting_engagements_heading': '협업 방식',
        'consulting_engagements_terms': '컨설팅만 수행하거나 선택한 소프트웨어 기능·라이선스를 포함할 수 있습니다. 결과 직접 조회나 후속 검토 기능의 제공 여부와 이용조건은 별도로 합의합니다.',
        'consulting_engagements_01_title': '프로젝트 단위 컨설팅',
        'consulting_engagements_01_application': '공항 확장, 항공사 이전, 공사 계획 등 범위가 정해진 계획 과업에 적용합니다.',
        'consulting_engagements_01_role': '모델 구축, 대안 비교 및 개선안 제안을 수행하고 계획·예산 검토에 활용할 결과를 정리합니다.',
        'consulting_engagements_02_title': '공동 제안·프로젝트 수행',
        'consulting_engagements_02_application': '설계·엔지니어링·컨설팅 과업의 시뮬레이션 및 처리용량 평가에 참여합니다.',
        'consulting_engagements_02_role': '제안 단계에서 방법, 역할, 일정 및 비용을 합의하고 수주 후 설계 검증과 대안 비교를 위한 분석을 수행합니다.',
        'consulting_engagements_03_title': '지속적 기술 파트너십',
        'consulting_engagements_03_application': '여러 공항 프로젝트에 걸친 전문 분석을 지원합니다.',
        'consulting_engagements_03_role': '합의된 기간 동안 설계 검토, 시나리오 분석 및 기술 자문을 제공하여 별도 사내 분석팀 없이도 과업을 지원합니다.',
        'consulting_deliverables_heading': '제공 결과물',
        'consulting_deliverables_usage_rights': '제공되는 데이터, 모델, 계정 및 솔루션 기능의 사용권과 이용기간은 과업별로 정합니다.',
        'consulting_deliverables_01_title': '컨설팅 보고서',
        'consulting_deliverables_01_use': '검토 목적, 대안 평가, 권고안 및 투자 우선순위를 담은 기술보고서 또는 경영진 요약본을 제공합니다.',
        'consulting_deliverables_02_title': 'HTML 웹 보고서',
        'consulting_deliverables_02_use': '브라우저에서 시나리오, 비교 결과 및 공간 시각화 자료를 확인할 수 있습니다.',
        'consulting_deliverables_03_title': 'PDF 및 DOCX',
        'consulting_deliverables_03_use': '과업 제출, 내부 검토, 공동 편집 및 인쇄 배포에 활용합니다.',
        'consulting_deliverables_04_title': '영상·렌더링 이미지',
        'consulting_deliverables_04_use': '회의와 이해관계자 설명을 위한 시뮬레이션 영상, 배치 대안 비교 및 공간 렌더링을 제공합니다.',
        'consulting_deliverables_05_title': '데이터·모델·선택 솔루션 구성요소',
        'consulting_deliverables_05_use': '과업에 맞춰 합의한 데이터셋, 모델 패키지, 접근 계정 또는 기능을 제공합니다.',
        'consulting_programme_heading': '일정과 비용',
        'consulting_programme_01_title': '프로젝트별 일정',
        'consulting_programme_01_description': '과업 범위, 자료 준비, 모델 검증 및 검토 과정을 고려하여 고객의 프로젝트 일정에 맞춥니다.',
        'consulting_programme_02_title': '기간제 지원',
        'consulting_programme_02_description': '1·3·6개월 등 합의된 기간 동안 설계 검토, 시나리오 분석 및 기술 자문을 제공하며 업무량, 지원 빈도와 응답시간은 별도로 합의합니다.',
        'consulting_programme_03_title': '단계별 수행',
        'consulting_programme_03_description': '구상, 기본설계, 실시설계 및 시공 단계에서 과업을 의뢰하고 계획 변경에 따라 추가 검토를 진행할 수 있습니다.',
        'consulting_programme_04_title': '비용 산정',
        'consulting_programme_04_description': '과업 범위, 프로젝트 규모, 기간, 대안 수 및 맞춤 개발 요구사항에 따라 비용을 정합니다.',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. 모든 권리 보유.',
        'flexa_about_title': 'Flexa 소개',
        'flexa_about_p1': 'Flexa는 공항 전문 솔루션 기업 TeamFlexa CO., LTD.의 브랜드입니다. 데이터로 복잡한 공항 운영을 해석하고 시뮬레이션 기술과 AI 기반 분석으로 최적의 결과를 제시합니다. 분석에 '
                          '그치지 않고 실제 운영 개선으로 이어지는 실행 가능한 인사이트를 제공합니다.',
        'flexa_about_p2': 'TeamFlexa는 인천국제공항의 사내벤처에서 출발하여 세계적인 공항 환경에서 쌓은 경험과 데이터를 활용합니다. Flexa 브랜드를 통해 터미널 운영 최적화부터 중장기 인프라 전략까지 컨설팅과 '
                          '솔루션을 제공하며, 고객이 복잡한 과제를 정량적으로 정의하고 가장 효과적인 결정을 내리도록 지원합니다.',
        'flexa_about_p3': '전 세계 공항, 공항 운영기관, 엔지니어링·건설사를 대상으로 문제를 빠르고 정확하게 진단하고 맞춤 전략을 설계하며 실행을 지원합니다. TeamFlexa는 공항 운영의 기준을 새롭게 제시하고 글로벌 '
                          '시장에서 데이터 기반 의사결정을 이끄는 파트너로 활동합니다.'},
 'zh': {'consulting_eyebrow': '咨询服务',
        'consulting_heading': '机场咨询',
        'consulting_intro': '为机场及工程团队提供规划、仿真与技术支持。',
        'consulting_projects_heading': '项目应用',
        'consulting_tab_overall': '概览',
        'consulting_tabs_aria': '咨询服务领域',
        'consulting_overall_intro': '典型项目涵盖新机场与新航站楼、扩建、不停航改造、航空公司或设施搬迁、分期投资及运行改善。',
        'consulting_overall_01_title': '航空公司搬迁',
        'consulting_overall_01_role': '评估值机、安检和中转设施能否满足搬迁航空公司的需求，并比较适宜的布局。',
        'consulting_overall_02_title': '新航站楼与机场扩建',
        'consulting_overall_02_role': '比较启用时间、设施规模以及新旧航站楼之间的功能分工。',
        'consulting_overall_03_title': '空侧布局调整',
        'consulting_overall_03_role': '评估滑行道和机位调整对飞机移动及地面保障车辆流动的影响。',
        'consulting_overall_04_title': '不停航改造',
        'consulting_overall_04_role': '评估哪些设施可同时关闭，并比较临时路线与施工顺序。',
        'consulting_overall_05_title': '设计与工程联合投标',
        'consulting_overall_05_role': '作为仿真与容量评估技术合作方参与投标，并在中标后开展约定的分析。',
        'consulting_overall_06_title': '机场发展战略',
        'consulting_overall_06_role': '评估需求、容量与备选方案，支持投资时机和设施规模决策。',
        'consulting_tab_demand': '需求与航班计划',
        'consulting_demand_intro': '将未来需求转化为运行情景、设施需求和扩建决策依据。',
        'consulting_task_01_title': '未来航空交通与旅客需求',
        'consulting_task_01_description': '利用现有预测与运行数据构建目标年和增长阶段情景，评估设施及运行需求。',
        'consulting_task_02_title': '设计日与高峰小时需求',
        'consulting_task_02_description': '将年需求转化为代表日、高峰日和逐时分布，确定设施需要承受的负荷。',
        'consulting_task_03_title': '未来航班计划生成',
        'consulting_task_03_description': '根据需求、机型组合、航空公司运营模式和运行时间生成设计日航班计划，并评估其运行可行性。',
        'consulting_task_04_title': '机型组合与航空公司运营模式',
        'consulting_task_04_description': '比较飞机大小、航空公司与航线组合、进出港航班波变化对登机口、机位和航站楼需求的影响。',
        'consulting_task_05_title': '旅客分群与到达分布',
        'consulting_task_05_description': '考虑到场规律与登机口分配，模拟出发、到达及中转旅客抵达各设施的时间和位置。',
        'consulting_task_06_title': '容量缺口与扩建触发条件',
        'consulting_task_06_description': '测试需求增长下的容量上限与剩余余量，提出扩建需求阈值、参考时间及设施优先级。',
        'consulting_tab_terminal': '航站楼与陆侧',
        'consulting_terminal_intro': '评估旅客处理、设施布局、航空公司搬迁、施工分期及交通衔接安排。',
        'consulting_task_07_title': '航站楼设施规模与适应性',
        'consulting_task_07_description': '依据需求与服务标准评估处理设施及候机空间，确定所需设施数量和运行时间。',
        'consulting_task_08_title': '出发流程与运行计划',
        'consulting_task_08_description': '比较值机、自助行李托运、登机牌查验、安检和出境边检的设施开放、运行时间及人员配置方案。',
        'consulting_task_09_title': '入境、行李提取与海关',
        'consulting_task_09_description': '联合模拟入境边检、行李提取和海关，评估单个环节变化对总处理时间及下游拥堵的影响。',
        'consulting_task_10_title': '中转流线与航站楼连接',
        'consulting_task_10_description': '评估中转安检、登机口间移动、连接通道和航站楼间交通站台的拥堵与衔接时间。',
        'consulting_task_11_title': '航空公司搬迁与设施影响',
        'consulting_task_11_description': '比较航空公司在航站楼、指廊、值机区或登机口间搬迁后的旅客分布、设施负荷、中转路线及候机区拥堵。',
        'consulting_task_12_title': '新航站楼与分期扩建',
        'consulting_task_12_description': '比较设施规模、布局、功能以及与既有航站楼的连接，评估启用及后续扩建阶段的容量。',
        'consulting_task_13_title': '机场不停航改造',
        'consulting_task_13_description': '评估设施关闭及可用设施减少的影响，确定可行的关闭组合与临时运行安排。',
        'consulting_task_14_title': '旅客流线与排队空间布局',
        'consulting_task_14_description': '从步行距离、拥堵和停留时间比较通道宽度、临时隔断、绕行路线与排队布局，并提出空间改善建议。',
        'consulting_task_15_title': '陆侧交通与换乘衔接',
        'consulting_task_15_description': '在约定范围内评估旅客与车辆到达情况，以及航站楼路侧、停车场、进出场道路和公共交通接口的布局方案。',
        'consulting_task_16_title': '复合条件与压力情景',
        'consulting_task_16_description': '组合高峰需求、航班延误、设施关闭及航空公司搬迁，识别薄弱区域并比较缓堵与恢复方案。',
        'consulting_tab_airside': '空侧',
        'consulting_airside_intro': '结合飞机与地面保障运行，评估跑道、滑行道、机位和配套设施规划。',
        'consulting_task_17_title': '跑道容量与航班延误',
        'consulting_task_17_description': '模拟运行模式、跑道占用、间隔和交通集中情况，评估含低能见度条件下的跑道吞吐量与进出港延误。',
        'consulting_task_18_title': '快速出口滑行道选址与布局',
        'consulting_task_18_description': '结合飞机着陆特性与跑道占用情况，比较快速出口滑行道的位置和间距。',
        'consulting_task_19_title': '空侧布局调整及影响',
        'consulting_task_19_description': '评估跑道、滑行道与机坪新建、延长、重新连接或关闭对路线、滑行时间、瓶颈及运行干扰的影响。',
        'consulting_task_20_title': '机位分配与同时推出',
        'consulting_task_20_description': '评估机型适配、近远机位分配、占用及同时移动，提出布局与运行备选方案。',
        'consulting_task_21_title': '飞机与地面保障车辆移动',
        'consulting_task_21_description': '将飞机移动和推出与车辆任务、路线一起模拟，评估服务道路拥堵、交叉干扰及车辆运行计划。',
        'consulting_task_22_title': '货运机坪与货机运行',
        'consulting_task_22_description': '评估大型货机机位适配、占用、进出路线以及与货运站和地面物流的连接。',
        'consulting_task_23_title': 'MRO、机库与GA/FBO通行',
        'consulting_task_23_description': '审查机型适配、机库进出、牵引路线以及与相邻机坪和服务道路的相互影响。',
        'consulting_task_24_title': '除冰设施布局与运行',
        'consulting_task_24_description': '评估同时容纳能力、进出路线与飞机净距，并比较不同处理时间下的排队及离港延误。',
        'consulting_task_25_title': '消防、供油及配套设施选址',
        'consulting_task_25_description': '评估救援消防、供油及公用设施的位置、通行路线和服务覆盖范围，支持布局与运行决策。',
        'consulting_task_26_title': '塔台视野与障碍物限制',
        'consulting_task_26_description': '在规划阶段比较视线与盲区，并审查跑道及周边设施规划涉及的障碍物限制面重叠。',
        'consulting_tab_digital': '数字孪生',
        'consulting_digital_intro': '模拟机场开发阶段、验证运行规则，并建立项目所需的分析功能。',
        'consulting_task_27_title': '现状与未来机场模型',
        'consulting_task_27_description': '准备空间输入数据，按各阶段规划设施建立现状、启用、阶段扩建及最终布局模型。',
        'consulting_task_28_title': '机场专属模型与运行验证',
        'consulting_task_28_description': '配置机场特有的布局、设施使用规则与运行程序，并依据可用观测数据和运行记录验证、校准。',
        'consulting_task_29_title': '设计叠加与空间渲染',
        'consulting_task_29_description': '比较现有规划、备选方案和施工阶段，以平面图、空间模型及仿真视频解释飞机、车辆和旅客流动。',
        'consulting_task_30_title': '定制KPI与分析功能',
        'consulting_task_30_description': '定义同时登机口运行、中转时间超限等机场专属指标，配置所需数据输入、输出和结果访问功能。',
        'consulting_scope_note': '根据机场数据、运行条件和项目要求，协商确定范围、模型详细程度及评估标准。额外研究、功能开发和外部系统集成的范围与所需进度一并商定。',
        'consulting_expertise_heading': '技术与机场经验',
        'consulting_expertise_origin': 'Team Flexa 起源于仁川国际机场公社的内部创业项目。团队参与过仁川机场的运行改善和扩建，以及公社海外机场业务中的相关项目。',
        'consulting_expertise_01_title': '自主软件',
        'consulting_expertise_01_description': '我们开发并拥有自己的软件，可按研究需求调整模型与功能，减少另购分析工具或招聘专业人员的需要。',
        'consulting_expertise_02_title': '定制KPI与分析功能',
        'consulting_expertise_02_description': '采用客户的绩效指标、评估标准和报告格式；现有功能不足时，协商额外开发或集成工作。',
        'consulting_expertise_03_title': '机场专属规则与布局',
        'consulting_expertise_03_description': '模拟航站楼连接、航空公司设施使用规则、机位配置、地面保障路线和分时限制。',
        'consulting_expertise_04_title': '现有数据与模型',
        'consulting_expertise_04_description': '利用可用机场、航班、设施数据和现有模型缩短准备时间，并依据客户观测数据及约定标准验证。',
        'consulting_expertise_05_title': '飞机、车辆与旅客流动联动',
        'consulting_expertise_05_description': '联合模拟飞机移动与车辆任务，通过登机口分配和旅客到达连接空侧及航站楼研究，评估设施变化的整体影响。',
        'consulting_engagements_heading': '合作方式',
        'consulting_engagements_terms': '可选择单独咨询，或咨询与指定软件功能、许可相结合的方式。直接访问结果或开展后续审查的功能及其使用条款另行商定。',
        'consulting_engagements_01_title': '项目制咨询',
        'consulting_engagements_01_application': '适用于机场扩建、航空公司搬迁、施工计划及其他明确的规划需求。',
        'consulting_engagements_01_role': '建立模型、比较方案并提出改善建议，为规划和预算审查准备成果。',
        'consulting_engagements_02_title': '联合投标与项目交付',
        'consulting_engagements_02_application': '承担设计、工程和咨询任务中的仿真与容量评估。',
        'consulting_engagements_02_role': '投标阶段商定方法、职责、进度和费用；中标后开展约定分析，验证设计并比较备选方案。',
        'consulting_engagements_03_title': '持续技术合作',
        'consulting_engagements_03_application': '为多个机场项目提供专业分析支持。',
        'consulting_engagements_03_role': '在约定期间提供设计审查、情景分析和技术咨询，无需客户组建专门的内部分析团队。',
        'consulting_deliverables_heading': '交付成果',
        'consulting_deliverables_usage_rights': '所提供数据、模型、账户或软件功能的使用权和期限按项目约定。',
        'consulting_deliverables_01_title': '咨询报告',
        'consulting_deliverables_01_use': '技术报告或管理层摘要，涵盖目标、方案评估、建议和投资优先级。',
        'consulting_deliverables_02_title': 'HTML网页报告',
        'consulting_deliverables_02_use': '通过浏览器查看情景、比较结果和空间可视化。',
        'consulting_deliverables_03_title': 'PDF与DOCX',
        'consulting_deliverables_03_use': '用于项目提交、内部审查、协作编辑和印刷分发。',
        'consulting_deliverables_04_title': '视频与渲染图像',
        'consulting_deliverables_04_use': '用于会议及利益相关方沟通的仿真视频、备选布局比较和空间渲染。',
        'consulting_deliverables_05_title': '数据、模型与指定软件组件',
        'consulting_deliverables_05_use': '按项目提供约定的数据集、模型包、访问账户或功能。',
        'consulting_programme_heading': '进度与费用',
        'consulting_programme_01_title': '项目进度安排',
        'consulting_programme_01_description': '结合研究范围、数据准备、模型验证和评审，将工作计划与客户项目进度协调。',
        'consulting_programme_02_title': '定期支持',
        'consulting_programme_02_description': '可在一个、三个或六个月等约定期间提供设计审查、情景分析和技术咨询；工作量、支持频率与响应时间另行商定。',
        'consulting_programme_03_title': '分阶段交付',
        'consulting_programme_03_description': '可在概念、初步设计、详细设计和施工阶段委托研究，并随规划变化开展补充审查。',
        'consulting_programme_04_title': '费用',
        'consulting_programme_04_description': '费用根据范围、项目规模、周期、备选方案数量和定制开发需求确定。',
        'footer_copyright': '版权所有 2026 TeamFlexa CO., LTD. 保留所有权利。',
        'flexa_about_title': '关于 Flexa',
        'flexa_about_p1': 'Flexa 是专业机场解决方案企业 TeamFlexa CO., LTD. 的品牌。我们通过数据解析复杂的机场运行，运用仿真技术与AI分析实现更优结果。我们的工作不仅是分析，更是提供能够推动实际运行改善的可执行见解。',
        'flexa_about_p2': 'TeamFlexa 起源于仁川国际机场的内部创业项目，运用来自全球领先机场环境的经验与数据。我们以 Flexa 品牌提供从航站楼运行优化到中长期基础设施战略的全流程咨询与解决方案，帮助客户量化复杂问题并做出最有效的决策。',
        'flexa_about_p3': '面向全球机场、机场运营机构及工程建设企业，TeamFlexa 快速、准确地诊断问题，制定定制战略并支持落实。我们重新定义机场运行标准，致力于成为全球市场中数据驱动决策的领先合作伙伴。'},
 'ja': {'consulting_eyebrow': 'コンサルティングサービス',
        'consulting_heading': '空港コンサルティング',
        'consulting_intro': '空港・エンジニアリングチームのための計画、シミュレーション、技術支援。',
        'consulting_projects_heading': 'プロジェクトへの適用',
        'consulting_tab_overall': '概要',
        'consulting_tabs_aria': 'コンサルティングの分野',
        'consulting_overall_intro': '新空港・新ターミナル、拡張、供用中の改修、航空会社・施設の移転、段階的投資、運用改善などに対応します。',
        'consulting_overall_01_title': '航空会社の移転',
        'consulting_overall_01_role': 'チェックイン・保安検査・乗り継ぎ施設が移転する航空会社を受け入れられるかを評価し、適切な配置を比較します。',
        'consulting_overall_02_title': '新ターミナルと空港拡張',
        'consulting_overall_02_role': '供用開始時期、施設規模、新旧ターミナル間の機能分担を比較します。',
        'consulting_overall_03_title': 'エアサイドの配置変更',
        'consulting_overall_03_role': '誘導路や駐機場の変更が、航空機の移動と地上支援車両の流れに与える影響を評価します。',
        'consulting_overall_04_title': '供用中の改修',
        'consulting_overall_04_role': '同時に閉鎖できる施設を評価し、仮設動線と施工順序を比較します。',
        'consulting_overall_05_title': '設計・エンジニアリングの共同提案',
        'consulting_overall_05_role': 'シミュレーションと容量評価の技術パートナーとして提案に参加し、受注後は合意した分析を実施します。',
        'consulting_overall_06_title': '空港開発戦略',
        'consulting_overall_06_role': '需要、容量、代替案を評価し、投資時期と施設規模の判断を支援します。',
        'consulting_tab_demand': '需要・運航スケジュール',
        'consulting_demand_intro': '将来需要を運用シナリオ、施設要件、拡張の判断につなげます。',
        'consulting_task_01_title': '将来の航空交通・旅客需要',
        'consulting_task_01_description': '既存の予測と運用データから目標年・成長段階別シナリオを作成し、施設と運用の要件を評価します。',
        'consulting_task_02_title': '設計日・ピーク時間の需要',
        'consulting_task_02_description': '年間需要を代表日・ピーク日・時間帯別の分布に展開し、施設が受け持つ負荷を把握します。',
        'consulting_task_03_title': '将来の運航スケジュール作成',
        'consulting_task_03_description': '需要、機種構成、航空会社の運用パターン、運用時間から設計日の運航スケジュールを作成し、実行可能性を評価します。',
        'consulting_task_04_title': '機種構成・航空会社の運用パターン',
        'consulting_task_04_description': '機体サイズ、航空会社・路線構成、発着便の集中がゲート・駐機場・ターミナル需要に与える影響を比較します。',
        'consulting_task_05_title': '旅客区分・到着分布',
        'consulting_task_05_description': '空港到着パターンとゲート割当を考慮し、出発・到着・乗り継ぎ旅客が各施設に到達する時刻と場所をモデル化します。',
        'consulting_task_06_title': '容量不足・拡張の判断基準',
        'consulting_task_06_description': '需要増加に対する容量上限と余力を検証し、拡張を検討する需要水準、時期の目安、施設の優先順位を提案します。',
        'consulting_tab_terminal': 'ターミナル・ランドサイド',
        'consulting_terminal_intro': '旅客処理、施設配置、航空会社移転、施工段階、アクセス計画を評価します。',
        'consulting_task_07_title': 'ターミナル施設の規模・適正性',
        'consulting_task_07_description': '需要とサービス基準に照らして処理施設と待合空間を評価し、必要な施設数と運用時間を明らかにします。',
        'consulting_task_08_title': '出発プロセス・運用計画',
        'consulting_task_08_description': 'チェックイン、自動手荷物預け、搭乗券確認、保安検査、出国審査の施設開放・運用時間・人員配置を比較します。',
        'consulting_task_09_title': '入国・手荷物受取・税関',
        'consulting_task_09_description': '入国審査、手荷物受取、税関を一体でモデル化し、各工程の変更が全体の処理時間と後続施設の混雑に与える影響を評価します。',
        'consulting_task_10_title': '乗り継ぎ動線・ターミナル接続',
        'consulting_task_10_description': '乗り継ぎ保安検査、ゲート間移動、連絡通路、ターミナル間交通の乗降場について、混雑と接続時間を評価します。',
        'consulting_task_11_title': '航空会社移転・施設への影響',
        'consulting_task_11_description': 'ターミナル・コンコース・チェックイン区画・ゲート間の移転に伴う旅客分布、施設負荷、乗り継ぎ経路、搭乗待合室の混雑を比較します。',
        'consulting_task_12_title': '新ターミナル・段階的拡張',
        'consulting_task_12_description': '施設規模、配置、役割、既存ターミナルとの接続を比較し、供用開始時とその後の拡張段階の容量を評価します。',
        'consulting_task_13_title': '空港供用中の改修',
        'consulting_task_13_description': '施設閉鎖と利用可能施設の減少を評価し、実行可能な閉鎖の組合せと暫定運用を検討します。',
        'consulting_task_14_title': '旅客動線・待ち行列の配置',
        'consulting_task_14_description': '通路幅、仮設壁、迂回路、待ち行列の配置を歩行距離・混雑・滞在時間で比較し、空間の改善を提案します。',
        'consulting_task_15_title': 'ランドサイドアクセス・交通接続',
        'consulting_task_15_description': '合意した範囲で旅客・車両の到着と、ターミナル乗降場、駐車場、アクセス道路、公共交通との接続配置を評価します。',
        'consulting_task_16_title': '複合条件・負荷シナリオ',
        'consulting_task_16_description': 'ピーク需要、便の遅延、施設閉鎖、航空会社移転を組み合わせ、弱点を特定して混雑緩和・回復策を比較します。',
        'consulting_tab_airside': 'エアサイド',
        'consulting_airside_intro': '滑走路、誘導路、駐機場、支援施設の計画を、航空機と地上支援の運用とともに評価します。',
        'consulting_task_17_title': '滑走路容量・運航遅延',
        'consulting_task_17_description': '運用方式、占有時間、間隔、交通集中をモデル化し、低視程を含む条件下の処理能力と発着遅延を評価します。',
        'consulting_task_18_title': '高速離脱誘導路の位置・配置',
        'consulting_task_18_description': '航空機の着陸特性と滑走路占有を考慮し、高速離脱誘導路の位置と間隔を比較します。',
        'consulting_task_19_title': 'エアサイド配置変更の影響',
        'consulting_task_19_description': '滑走路・誘導路・エプロンの新設、延伸、再接続、閉鎖が経路、地上走行時間、ボトルネック、運用干渉に与える影響を評価します。',
        'consulting_task_20_title': '駐機場割当・同時プッシュバック',
        'consulting_task_20_description': '機種適合性、コンタクト・リモートスポットの割当、占有、同時移動を評価し、配置と運用の代替案を提案します。',
        'consulting_task_21_title': '航空機・地上支援車両の移動',
        'consulting_task_21_description': '航空機の移動・プッシュバックと車両の作業・経路を一体でモデル化し、サービス道路の混雑、交差干渉、車両運用計画を評価します。',
        'consulting_task_22_title': '貨物エプロン・貨物機運用',
        'consulting_task_22_description': '大型貨物機のスポット適合性、占有、進入経路、貨物ターミナルや地上物流との接続を評価します。',
        'consulting_task_23_title': 'MRO・格納庫・GA/FBOアクセス',
        'consulting_task_23_description': '機種適合性、格納庫へのアクセス、牽引経路、隣接エプロンやサービス道路との相互作用を検討します。',
        'consulting_task_24_title': '除氷施設の配置・運用',
        'consulting_task_24_description': '同時収容、進入・退出経路、航空機のクリアランスを評価し、処理時間の変動による待ち行列と出発遅延を比較します。',
        'consulting_task_25_title': '消防・給油・支援施設の立地',
        'consulting_task_25_description': '救難消防、給油、ユーティリティ施設の位置、アクセス経路、サービス範囲を評価し、配置と運用の判断を支援します。',
        'consulting_task_26_title': '管制塔の視界・障害物制限',
        'consulting_task_26_description': '計画段階で視線と死角を比較し、滑走路や周辺施設計画に関連する障害物制限表面の重なりを検討します。',
        'consulting_tab_digital': 'デジタルツイン',
        'consulting_digital_intro': '空港の開発段階をモデル化し、運用ルールを検証して、プロジェクトに必要な分析機能を構築します。',
        'consulting_task_27_title': '現在・将来の空港モデル',
        'consulting_task_27_description': '空間入力データを準備し、各段階の計画施設を反映した現況、供用開始、中間拡張、最終形の配置をモデル化します。',
        'consulting_task_28_title': '空港固有モデル・運用検証',
        'consulting_task_28_description': '固有の配置、施設利用ルール、運用手順を設定し、利用可能な観測データや運用記録に照らして検証・調整します。',
        'consulting_task_29_title': '設計の重ね合わせ・空間描画',
        'consulting_task_29_description': '既存計画、代替案、施工段階を比較し、平面図、空間モデル、シミュレーション動画で航空機・車両・旅客の流れを説明します。',
        'consulting_task_30_title': '独自KPI・分析機能',
        'consulting_task_30_description': 'ゲート同時運用、乗り継ぎ時間超過などの空港固有指標を定義し、必要なデータ入出力と結果参照機能を設定します。',
        'consulting_scope_note': '業務範囲、モデルの詳細度、評価基準は、空港データ、運用条件、プロジェクト要件に基づき合意します。追加調査、機能開発、外部システム連携は必要な日程とともに範囲を定めます。',
        'consulting_expertise_heading': '技術と空港での経験',
        'consulting_expertise_origin': 'Team Flexa は仁川国際空港公社の社内ベンチャープログラムから生まれました。チームは仁川空港の運用改善・拡張や、公社の海外空港事業における業務を経験しています。',
        'consulting_expertise_01_title': '自社開発ソフトウェア',
        'consulting_expertise_01_description': '自社で開発・保有するソフトウェアを用い、調査に合わせてモデルや機能を調整することで、別途の分析ツール導入や専門人材確保の負担を減らします。',
        'consulting_expertise_02_title': '独自KPI・分析機能',
        'consulting_expertise_02_description': 'お客様の業績指標、評価基準、報告形式を用い、既存機能で不足する場合は追加開発や連携を合意します。',
        'consulting_expertise_03_title': '空港固有のルール・配置',
        'consulting_expertise_03_description': 'ターミナル接続、航空会社の施設利用ルール、駐機場構成、地上支援経路、時間帯別の制約をモデル化します。',
        'consulting_expertise_04_title': '既存データ・モデルの活用',
        'consulting_expertise_04_description': '利用可能な空港・運航・施設データと既存モデルで準備時間を短縮し、お客様の観測データと合意した基準で検証します。',
        'consulting_expertise_05_title': '航空機・車両・旅客の流れを連携',
        'consulting_expertise_05_description': '航空機移動と車両作業を一体でモデル化し、ゲート割当・旅客到着を通じてエアサイドとターミナルの分析をつなぎ、施設変更の広域的な影響を評価します。',
        'consulting_engagements_heading': '協業の進め方',
        'consulting_engagements_terms': 'コンサルティング単独、または選択したソフトウェア機能・ライセンスとの組合せで提供します。結果への直接アクセスや継続検討用機能、および利用条件は別途合意します。',
        'consulting_engagements_01_title': 'プロジェクト単位のコンサルティング',
        'consulting_engagements_01_application': '空港拡張、航空会社移転、施工計画など、範囲の定まった計画課題に対応します。',
        'consulting_engagements_01_role': 'モデルを構築して案を比較し、改善を提案するとともに、計画・予算の検討に向けて結果をまとめます。',
        'consulting_engagements_02_title': '共同提案・プロジェクト遂行',
        'consulting_engagements_02_application': '設計、エンジニアリング、コンサルティング業務におけるシミュレーションと容量評価を担います。',
        'consulting_engagements_02_role': '提案段階で手法、責任分担、工程、費用を合意し、受注後に設計検証と代替案比較のための分析を実施します。',
        'consulting_engagements_03_title': '継続的な技術パートナーシップ',
        'consulting_engagements_03_application': '複数の空港プロジェクトにわたる専門分析を提供します。',
        'consulting_engagements_03_role': '合意した期間中、設計レビュー、シナリオ分析、技術助言を提供し、専任の社内分析チームを置かずに支援を受けられます。',
        'consulting_deliverables_heading': '成果物',
        'consulting_deliverables_usage_rights': '提供データ、モデル、アカウント、ソリューション機能の利用権と期間は、契約ごとに定めます。',
        'consulting_deliverables_01_title': 'コンサルティング報告書',
        'consulting_deliverables_01_use': '目的、代替案評価、提言、投資優先順位をまとめた技術報告書または経営層向け要約を提供します。',
        'consulting_deliverables_02_title': 'HTMLウェブレポート',
        'consulting_deliverables_02_use': 'シナリオ、比較結果、空間可視化をブラウザーで確認できます。',
        'consulting_deliverables_03_title': 'PDF・DOCX',
        'consulting_deliverables_03_use': 'プロジェクト提出、社内レビュー、共同編集、印刷配布に利用できます。',
        'consulting_deliverables_04_title': '動画・レンダリング画像',
        'consulting_deliverables_04_use': '会議や関係者への説明に向けたシミュレーション動画、配置案比較、空間レンダリングを提供します。',
        'consulting_deliverables_05_title': 'データ・モデル・選択した機能',
        'consulting_deliverables_05_use': '契約で合意したデータセット、モデル一式、アクセスアカウントまたは機能を提供します。',
        'consulting_programme_heading': '日程と費用',
        'consulting_programme_01_title': 'プロジェクト別の日程',
        'consulting_programme_01_description': '業務範囲、データ準備、モデル検証、レビューを考慮して、お客様のプロジェクト日程に合わせます。',
        'consulting_programme_02_title': '期間を定めた支援',
        'consulting_programme_02_description': '1・3・6か月など合意した期間、設計レビュー、シナリオ分析、技術助言を提供し、業務量、支援頻度、応答時間は別途定めます。',
        'consulting_programme_03_title': '段階別の実施',
        'consulting_programme_03_description': '構想、基本設計、詳細設計、施工の各段階で調査を依頼でき、計画変更に応じて追加レビューを実施します。',
        'consulting_programme_04_title': '料金',
        'consulting_programme_04_description': '業務範囲、規模、期間、比較案の数、個別開発の要件に応じて費用を定めます。',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. 無断転載を禁じます。',
        'flexa_about_title': 'Flexaについて',
        'flexa_about_p1': 'Flexa は空港ソリューション専門企業 TeamFlexa CO., LTD. '
                          'のブランドです。データを通じて空港運用の複雑さを読み解き、シミュレーション技術とAIによる分析で最適な成果を導きます。分析にとどまらず、実際の運用改善につながる実行可能な知見を提供します。',
        'flexa_about_p2': '仁川国際空港の社内ベンチャーから生まれた TeamFlexa は、世界有数の空港環境で蓄積した経験とデータを活用します。Flexa '
                          'ブランドのもと、ターミナル運用の最適化から中長期のインフラ戦略まで一貫したコンサルティングとソリューションを提供し、複雑な課題を定量的に捉えて最も効果的な意思決定を行えるよう支援します。',
        'flexa_about_p3': 'TeamFlexa '
                          'は世界の空港、空港運営機関、エンジニアリング・建設会社に対し、迅速かつ的確な課題診断、個別の戦略策定、実行支援を行います。空港運用の基準を新たに示し、世界市場におけるデータに基づく意思決定を牽引するパートナーを目指しています。'},
 'es': {'consulting_eyebrow': 'Servicios de consultoría',
        'consulting_heading': 'Consultoría aeroportuaria',
        'consulting_intro': 'Planificación, simulación y apoyo técnico para aeropuertos y equipos de ingeniería.',
        'consulting_projects_heading': 'Aplicaciones en proyectos',
        'consulting_tab_overall': 'Visión general',
        'consulting_tabs_aria': 'Áreas de consultoría',
        'consulting_overall_intro': 'Trabajamos en proyectos de nuevos aeropuertos y terminales, ampliación, renovación sin interrumpir '
                                    'las operaciones, traslado de aerolíneas o instalaciones, inversión por fases y mejora operativa.',
        'consulting_overall_01_title': 'Traslado de aerolíneas',
        'consulting_overall_01_role': 'Evaluar si las instalaciones de facturación, seguridad y conexiones pueden atender a las aerolíneas '
                                      'trasladadas y comparar distribuciones adecuadas.',
        'consulting_overall_02_title': 'Nuevas terminales y ampliación aeroportuaria',
        'consulting_overall_02_role': 'Comparar fechas de apertura, dimensiones de las instalaciones y reparto de funciones entre las '
                                      'terminales nuevas y existentes.',
        'consulting_overall_03_title': 'Cambios en la configuración del lado aire',
        'consulting_overall_03_role': 'Evaluar cómo los cambios en calles de rodaje y puestos de estacionamiento afectan al movimiento de '
                                      'aeronaves y a los flujos de vehículos de asistencia en tierra.',
        'consulting_overall_04_title': 'Renovación sin interrumpir las operaciones',
        'consulting_overall_04_role': 'Evaluar qué instalaciones pueden cerrarse simultáneamente y comparar rutas provisionales y '
                                      'secuencias de obra.',
        'consulting_overall_05_title': 'Propuestas conjuntas de diseño e ingeniería',
        'consulting_overall_05_role': 'Participar en propuestas como socio técnico de simulación y evaluación de capacidad, y realizar los '
                                      'análisis acordados tras la adjudicación.',
        'consulting_overall_06_title': 'Estrategia de desarrollo aeroportuario',
        'consulting_overall_06_role': 'Evaluar la demanda, la capacidad y las alternativas para fundamentar el calendario de inversión y '
                                      'el dimensionamiento de las instalaciones.',
        'consulting_tab_demand': 'Demanda y horarios',
        'consulting_demand_intro': 'Traducir la demanda futura en escenarios operativos, necesidades de instalaciones y decisiones de '
                                   'ampliación.',
        'consulting_task_01_title': 'Demanda futura de tráfico y pasajeros',
        'consulting_task_01_description': 'Desarrollar escenarios para el año horizonte y las distintas etapas de crecimiento a partir de '
                                          'previsiones y datos operativos existentes, para evaluar las necesidades de instalaciones y '
                                          'operación.',
        'consulting_task_02_title': 'Demanda del día de diseño y de la hora punta',
        'consulting_task_02_description': 'Convertir la demanda anual en perfiles de día representativo, día punta y demanda horaria para '
                                          'establecer las cargas que deben atender las instalaciones.',
        'consulting_task_03_title': 'Generación de horarios de vuelo futuros',
        'consulting_task_03_description': 'Elaborar horarios para el día de diseño a partir de la demanda, la composición de la flota, los '
                                          'patrones de las aerolíneas y los horarios de operación, y evaluar su viabilidad operativa.',
        'consulting_task_04_title': 'Composición de la flota y patrones de las aerolíneas',
        'consulting_task_04_description': 'Comparar cómo el tamaño de las aeronaves, la combinación de aerolíneas y rutas, y las oleadas '
                                          'de llegadas y salidas afectan a la demanda de puertas de embarque, puestos de estacionamiento y '
                                          'terminales.',
        'consulting_task_05_title': 'Segmentos de pasajeros y perfiles de llegada',
        'consulting_task_05_description': 'Modelar cuándo y dónde llegan los pasajeros de salida, llegada y conexión a las instalaciones, '
                                          'teniendo en cuenta los patrones de presentación y la asignación de puertas.',
        'consulting_task_06_title': 'Déficits de capacidad y umbrales de ampliación',
        'consulting_task_06_description': 'Contrastar el crecimiento de la demanda con los límites y la capacidad disponible para '
                                          'recomendar umbrales de ampliación, plazos orientativos y prioridades de instalaciones.',
        'consulting_tab_terminal': 'Terminal y lado tierra',
        'consulting_terminal_intro': 'Evaluar los procesos de pasajeros, la distribución de instalaciones, el traslado de aerolíneas, las '
                                     'fases de obra y las soluciones de acceso.',
        'consulting_task_07_title': 'Dimensionamiento y adecuación de las instalaciones de la terminal',
        'consulting_task_07_description': 'Evaluar las instalaciones de procesamiento y las zonas de espera frente a la demanda y los '
                                          'criterios de servicio para determinar las cantidades necesarias y los horarios de operación.',
        'consulting_task_08_title': 'Procesos de salida y planes operativos',
        'consulting_task_08_description': 'Comparar la apertura de instalaciones, los horarios y la dotación de personal para facturación, '
                                          'entrega automática de equipaje, control de tarjetas de embarque, seguridad y control migratorio '
                                          'de salida.',
        'consulting_task_09_title': 'Llegadas, recogida de equipaje y aduanas',
        'consulting_task_09_description': 'Modelar conjuntamente el control migratorio de llegada, la recogida de equipaje y las aduanas '
                                          'para evaluar cómo los cambios en una etapa afectan al tiempo total de procesamiento y a la '
                                          'congestión en las etapas posteriores.',
        'consulting_task_10_title': 'Flujos de conexión y enlaces entre terminales',
        'consulting_task_10_description': 'Evaluar la congestión y los tiempos de conexión en los controles de seguridad de tránsito, los '
                                          'recorridos entre puertas, los pasillos y los andenes del transporte entre terminales.',
        'consulting_task_11_title': 'Traslado de aerolíneas e impacto en las instalaciones',
        'consulting_task_11_description': 'Comparar traslados de aerolíneas entre terminales, muelles, zonas de facturación o puertas, '
                                          'considerando la distribución de pasajeros, las cargas de las instalaciones, los recorridos de '
                                          'conexión y la congestión en las salas de embarque.',
        'consulting_task_12_title': 'Nuevas terminales y ampliación por fases',
        'consulting_task_12_description': 'Comparar las dimensiones, la distribución, las funciones y las conexiones con las terminales '
                                          'existentes para evaluar la capacidad en la apertura y en las fases posteriores de ampliación.',
        'consulting_task_13_title': 'Renovación con el aeropuerto en funcionamiento',
        'consulting_task_13_description': 'Evaluar cierres y reducciones de disponibilidad para determinar qué combinaciones de cierres y '
                                          'soluciones operativas provisionales son viables.',
        'consulting_task_14_title': 'Circulación de pasajeros y distribución de colas',
        'consulting_task_14_description': 'Comparar anchuras de pasillos, separaciones, desvíos y distribuciones de colas según la '
                                          'distancia recorrida, la congestión y el tiempo de permanencia, y recomendar mejoras en la '
                                          'distribución del espacio.',
        'consulting_task_15_title': 'Accesos terrestres y conexiones de transporte',
        'consulting_task_15_description': 'Evaluar las llegadas de pasajeros y vehículos y las alternativas de distribución para las zonas '
                                          'de subida y bajada de pasajeros, los aparcamientos, las vías de acceso y las conexiones con el '
                                          'transporte público, dentro del alcance acordado.',
        'consulting_task_16_title': 'Condiciones combinadas y escenarios de alta exigencia',
        'consulting_task_16_description': 'Combinar demanda punta, retrasos de vuelos, cierres y traslados de aerolíneas para identificar '
                                          'zonas vulnerables y comparar opciones de alivio de la congestión y recuperación operativa.',
        'consulting_tab_airside': 'Lado aire',
        'consulting_airside_intro': 'Evaluar los planes de pistas, calles de rodaje, puestos de estacionamiento e instalaciones auxiliares '
                                    'junto con las operaciones de aeronaves y asistencia en tierra.',
        'consulting_task_17_title': 'Capacidad de pista y retrasos de vuelos',
        'consulting_task_17_description': 'Modelar modos de operación, ocupación, separación y concentraciones de tráfico para evaluar la '
                                          'capacidad de pista y los retrasos de llegadas y salidas, incluidas las condiciones de baja '
                                          'visibilidad.',
        'consulting_task_18_title': 'Ubicación y diseño de calles de salida rápida',
        'consulting_task_18_description': 'Comparar la ubicación y separación de las calles de salida rápida según las características de '
                                          'aterrizaje de las aeronaves y la ocupación de pista.',
        'consulting_task_19_title': 'Cambios en la configuración del lado aire y sus efectos',
        'consulting_task_19_description': 'Evaluar cómo las pistas, calles de rodaje y plataformas nuevas, ampliadas, reconectadas o '
                                          'cerradas afectan a las rutas, los tiempos de rodaje, los cuellos de botella y las '
                                          'interferencias operativas.',
        'consulting_task_20_title': 'Asignación de puestos y retrocesos simultáneos',
        'consulting_task_20_description': 'Evaluar la compatibilidad de aeronaves, la asignación de puestos de contacto y remotos, la '
                                          'ocupación y los movimientos simultáneos para recomendar alternativas de distribución y '
                                          'operación.',
        'consulting_task_21_title': 'Movimientos de aeronaves y vehículos de asistencia en tierra',
        'consulting_task_21_description': 'Modelar los movimientos y retrocesos de aeronaves junto con las tareas y rutas de los vehículos '
                                          'para evaluar la congestión de las vías de servicio, las interferencias en los cruces y los '
                                          'planes operativos de los vehículos.',
        'consulting_task_22_title': 'Plataformas de carga y operaciones de cargueros',
        'consulting_task_22_description': 'Evaluar la compatibilidad de los puestos para grandes aeronaves de carga, su ocupación, las '
                                          'rutas de acceso y las conexiones con las terminales de carga y la logística terrestre.',
        'consulting_task_23_title': 'Acceso a MRO, hangares y GA/FBO',
        'consulting_task_23_description': 'Revisar la compatibilidad de aeronaves, el acceso a hangares, las rutas de remolque y las '
                                          'interacciones con plataformas y vías de servicio adyacentes.',
        'consulting_task_24_title': 'Distribución y operación de instalaciones de deshielo',
        'consulting_task_24_description': 'Evaluar la capacidad para atender aeronaves simultáneamente, las rutas de entrada y salida y '
                                          'las distancias de seguridad, y comparar colas y retrasos de salida con tiempos de tratamiento '
                                          'variables.',
        'consulting_task_25_title': 'Ubicación de ARFF, combustible e instalaciones auxiliares',
        'consulting_task_25_description': 'Evaluar la ubicación de las instalaciones de salvamento y extinción de incendios, combustible y '
                                          'servicios, sus rutas de acceso y su cobertura para fundamentar decisiones de distribución y '
                                          'operación.',
        'consulting_task_26_title': 'Visibilidad desde la torre y limitaciones por obstáculos',
        'consulting_task_26_description': 'Comparar líneas de visión y puntos ciegos, y revisar, en la fase de planificación, las '
                                          'interferencias con las superficies limitadoras de obstáculos asociadas a los planes de pistas e '
                                          'instalaciones del entorno.',
        'consulting_tab_digital': 'Gemelos digitales',
        'consulting_digital_intro': 'Modelar las etapas de desarrollo del aeropuerto, validar las reglas operativas y desarrollar las '
                                    'capacidades de análisis que requiere el proyecto.',
        'consulting_task_27_title': 'Modelos actuales y futuros del aeropuerto',
        'consulting_task_27_description': 'Preparar los datos espaciales y modelar las configuraciones existentes, de apertura, de '
                                          'ampliación intermedia y de desarrollo final, con las instalaciones previstas en cada etapa.',
        'consulting_task_28_title': 'Modelos específicos del aeropuerto y validación operativa',
        'consulting_task_28_description': 'Configurar distribuciones particulares, reglas de uso de instalaciones y procedimientos '
                                          'operativos, y validar y calibrar los modelos con las observaciones y los registros operativos '
                                          'disponibles.',
        'consulting_task_29_title': 'Superposición de diseños y visualización espacial',
        'consulting_task_29_description': 'Comparar planes existentes, alternativas y fases de obra, y explicar los flujos de aeronaves, '
                                          'vehículos y pasajeros mediante vistas en planta, modelos espaciales y vídeos de simulación.',
        'consulting_task_30_title': 'KPI y funciones de análisis a medida',
        'consulting_task_30_description': 'Definir indicadores específicos del aeropuerto, incluidas las operaciones simultáneas en '
                                          'puertas y los excesos del tiempo de conexión, y configurar los datos de entrada, los resultados '
                                          'y las funciones de acceso necesarios.',
        'consulting_scope_note': 'El alcance, el nivel de detalle del modelo y los criterios de evaluación se acuerdan según los datos del '
                                 'aeropuerto, las condiciones operativas y los requisitos del proyecto. Los estudios adicionales, el '
                                 'desarrollo de funciones y la integración con sistemas externos se definen junto con el calendario '
                                 'necesario.',
        'consulting_expertise_heading': 'Tecnología y experiencia aeroportuaria',
        'consulting_expertise_origin': 'Team Flexa surgió del programa de emprendimiento interno de Incheon International Airport '
                                       'Corporation. Nuestro equipo ha trabajado en la mejora operativa y la ampliación del Aeropuerto de '
                                       'Incheon, así como en proyectos del negocio aeroportuario internacional de la corporación.',
        'consulting_expertise_01_title': 'Software propio',
        'consulting_expertise_01_description': 'Desarrollamos y somos propietarios de nuestro software; adaptamos los modelos y las '
                                               'funciones al estudio y reducimos la necesidad de herramientas de análisis adicionales o '
                                               'personal especializado.',
        'consulting_expertise_02_title': 'KPI y funciones de análisis a medida',
        'consulting_expertise_02_description': 'Utilizamos sus indicadores de rendimiento, criterios de evaluación y formatos de informe, '
                                               'y acordamos desarrollos o integraciones adicionales cuando las funciones existentes no son '
                                               'suficientes.',
        'consulting_expertise_03_title': 'Reglas y distribuciones específicas de cada aeropuerto',
        'consulting_expertise_03_description': 'Modelamos conexiones entre terminales, reglas de uso de instalaciones por aerolínea, '
                                               'configuraciones de puestos, rutas de asistencia en tierra y restricciones horarias.',
        'consulting_expertise_04_title': 'Datos y modelos existentes',
        'consulting_expertise_04_description': 'Utilizamos los datos disponibles de aeropuertos, vuelos e instalaciones y los modelos '
                                               'existentes para reducir el tiempo de preparación, validándolos con sus observaciones y los '
                                               'criterios acordados.',
        'consulting_expertise_05_title': 'Flujos conectados de aeronaves, vehículos y pasajeros',
        'consulting_expertise_05_description': 'Modelamos conjuntamente los movimientos de aeronaves y las tareas de los vehículos; las '
                                               'asignaciones de puertas y las llegadas de pasajeros vinculan los estudios del lado aire y '
                                               'de la terminal para evaluar los efectos más amplios de los cambios en las instalaciones.',
        'consulting_engagements_heading': 'Cómo colaborar con nosotros',
        'consulting_engagements_terms': 'Ofrecemos servicios de consultoría, solos o junto con determinadas funciones o licencias de '
                                        'software. El acceso directo a los resultados o a funciones de revisión posterior y sus '
                                        'condiciones de uso se acuerdan por separado.',
        'consulting_engagements_01_title': 'Consultoría por proyecto',
        'consulting_engagements_01_application': 'Ampliación aeroportuaria, traslado de aerolíneas, planes de obra y otras necesidades de '
                                                 'planificación definidas.',
        'consulting_engagements_01_role': 'Desarrollamos modelos, comparamos opciones y recomendamos mejoras, con resultados preparados '
                                          'para la revisión de planes y presupuestos.',
        'consulting_engagements_02_title': 'Propuestas conjuntas y ejecución de proyectos',
        'consulting_engagements_02_application': 'Simulación y evaluación de capacidad en proyectos de diseño, ingeniería y consultoría.',
        'consulting_engagements_02_role': 'En la fase de propuesta, acordamos el método, las responsabilidades, el calendario y los '
                                          'honorarios; tras la adjudicación, realizamos los análisis acordados para comprobar los diseños '
                                          'y comparar alternativas.',
        'consulting_engagements_03_title': 'Colaboración técnica continuada',
        'consulting_engagements_03_application': 'Análisis especializado para múltiples proyectos aeroportuarios.',
        'consulting_engagements_03_role': 'Ofrecemos revisión de diseños, análisis de escenarios y asesoramiento técnico durante un '
                                          'periodo acordado, sin necesidad de un equipo interno dedicado al análisis.',
        'consulting_deliverables_heading': 'Entregables',
        'consulting_deliverables_usage_rights': 'Los derechos y plazos de uso de los datos, modelos, cuentas o funciones suministrados se '
                                                'definen para cada encargo.',
        'consulting_deliverables_01_title': 'Informes de consultoría',
        'consulting_deliverables_01_use': 'Informes técnicos o resúmenes ejecutivos con objetivos, evaluación de alternativas, '
                                          'recomendaciones y prioridades de inversión.',
        'consulting_deliverables_02_title': 'Informes web en HTML',
        'consulting_deliverables_02_use': 'Revisión de escenarios, comparaciones y visualizaciones espaciales desde el navegador.',
        'consulting_deliverables_03_title': 'PDF y DOCX',
        'consulting_deliverables_03_use': 'Presentación de documentación del proyecto, revisión interna, edición colaborativa y '
                                          'distribución impresa.',
        'consulting_deliverables_04_title': 'Vídeos e imágenes renderizadas',
        'consulting_deliverables_04_use': 'Vídeos de simulación, comparaciones de distribuciones alternativas y representaciones '
                                          'espaciales para reuniones y comunicación con las partes interesadas.',
        'consulting_deliverables_05_title': 'Datos, modelos y componentes seleccionados de la solución',
        'consulting_deliverables_05_use': 'Conjuntos de datos, paquetes de modelos, cuentas de acceso o funciones acordados para el '
                                          'encargo.',
        'consulting_programme_heading': 'Calendario y honorarios',
        'consulting_programme_01_title': 'Calendario adaptado al proyecto',
        'consulting_programme_01_description': 'Ajustamos el calendario a su proyecto, teniendo en cuenta el alcance del estudio, la '
                                               'preparación de datos, la validación del modelo y las revisiones.',
        'consulting_programme_02_title': 'Apoyo por un periodo determinado',
        'consulting_programme_02_description': 'La revisión de diseños, el análisis de escenarios y el asesoramiento técnico están '
                                               'disponibles durante periodos acordados, por ejemplo, de uno, tres o seis meses; la carga '
                                               'de trabajo, la frecuencia y los plazos de respuesta se acuerdan por separado.',
        'consulting_programme_03_title': 'Entregas por fases',
        'consulting_programme_03_description': 'Encargue estudios en las etapas de concepto, diseño preliminar, diseño de detalle y '
                                               'construcción, con revisiones adicionales a medida que cambien los planes.',
        'consulting_programme_04_title': 'Honorarios',
        'consulting_programme_04_description': 'Los honorarios dependen del alcance, la escala del proyecto, la duración, el número de '
                                               'alternativas y los requisitos de desarrollo a medida.',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. Todos los derechos reservados.',
        'flexa_about_title': 'Quién es Flexa',
        'flexa_about_p1': 'Flexa es una marca de TeamFlexa CO., LTD., una empresa especializada en soluciones aeroportuarias que utiliza '
                          'los datos para comprender la complejidad de las operaciones y ofrecer resultados óptimos mediante tecnologías '
                          'de simulación y análisis basado en IA. Vamos más allá del análisis y aportamos conclusiones prácticas que se '
                          'traducen en mejoras operativas reales.',
        'flexa_about_p2': 'TeamFlexa nació como una iniciativa de emprendimiento interno en el Aeropuerto Internacional de Incheon y se '
                          'apoya en la experiencia y los datos de uno de los entornos aeroportuarios más destacados del mundo. Bajo la '
                          'marca Flexa, ofrecemos consultoría y soluciones integrales, desde la optimización de las operaciones de la '
                          'terminal hasta la estrategia de infraestructuras a medio y largo plazo. Ayudamos a nuestros clientes a definir '
                          'cuantitativamente los retos complejos y a tomar las decisiones más eficaces.',
        'flexa_about_p3': 'Al servicio de aeropuertos, operadores aeroportuarios y empresas de ingeniería y construcción de todo el mundo, '
                          'TeamFlexa diagnostica problemas con rapidez y precisión, diseña estrategias a medida y garantiza su ejecución. '
                          'Redefinimos los estándares de las operaciones aeroportuarias y somos un socio de referencia para la toma de '
                          'decisiones basada en datos en el mercado global.'},
 'th': {'consulting_eyebrow': 'บริการที่ปรึกษา',
        'consulting_heading': 'ที่ปรึกษาด้านท่าอากาศยาน',
        'consulting_intro': 'การวางแผน การจำลอง และการสนับสนุนทางเทคนิคสำหรับท่าอากาศยานและทีมวิศวกรรม',
        'consulting_projects_heading': 'การประยุกต์ใช้ในโครงการ',
        'consulting_tab_overall': 'ภาพรวม',
        'consulting_tabs_aria': 'ขอบเขตบริการที่ปรึกษา',
        'consulting_overall_intro': 'โครงการที่รองรับ ได้แก่ ท่าอากาศยานและอาคารผู้โดยสารใหม่ การขยายและปรับปรุงขณะเปิดดำเนินงาน '
                                    'การย้ายสายการบินหรือสิ่งอำนวยความสะดวก การลงทุนเป็นระยะ และการปรับปรุงการดำเนินงาน',
        'consulting_overall_01_title': 'การย้ายสายการบิน',
        'consulting_overall_01_role': 'ประเมินว่าจุดเช็กอิน จุดตรวจความปลอดภัย '
                                      'และสิ่งอำนวยความสะดวกสำหรับการเปลี่ยนเครื่องรองรับสายการบินที่ย้ายมาได้หรือไม่ '
                                      'พร้อมเปรียบเทียบผังที่เหมาะสม',
        'consulting_overall_02_title': 'อาคารผู้โดยสารใหม่และการขยายท่าอากาศยาน',
        'consulting_overall_02_role': 'เปรียบเทียบกำหนดเปิดใช้ ขนาดสิ่งอำนวยความสะดวก '
                                      'และการแบ่งหน้าที่ระหว่างอาคารผู้โดยสารใหม่กับอาคารเดิม',
        'consulting_overall_03_title': 'การปรับผังเขตการบิน',
        'consulting_overall_03_role': 'ประเมินผลของการปรับทางขับและหลุมจอดต่อการเคลื่อนที่ของอากาศยานและรถบริการภาคพื้น',
        'consulting_overall_04_title': 'การปรับปรุงขณะเปิดดำเนินงาน',
        'consulting_overall_04_role': 'ประเมินว่าสิ่งอำนวยความสะดวกใดปิดพร้อมกันได้ และเปรียบเทียบเส้นทางชั่วคราวกับลำดับงานก่อสร้าง',
        'consulting_overall_05_title': 'ข้อเสนอร่วมด้านออกแบบและวิศวกรรม',
        'consulting_overall_05_role': 'ร่วมจัดทำข้อเสนอในฐานะพันธมิตรทางเทคนิคด้านการจำลองและประเมินขีดความสามารถ '
                                      'แล้วดำเนินการวิเคราะห์ตามที่ตกลงเมื่อได้รับงาน',
        'consulting_overall_06_title': 'กลยุทธ์การพัฒนาท่าอากาศยาน',
        'consulting_overall_06_role': 'ประเมินอุปสงค์ ขีดความสามารถ และทางเลือก เพื่อประกอบการกำหนดช่วงเวลาลงทุนและขนาดสิ่งอำนวยความสะดวก',
        'consulting_tab_demand': 'อุปสงค์และตารางบิน',
        'consulting_demand_intro': 'แปลงอุปสงค์ในอนาคตเป็นสถานการณ์ดำเนินงาน ความต้องการสิ่งอำนวยความสะดวก และข้อมูลประกอบการตัดสินใจขยาย',
        'consulting_task_01_title': 'ปริมาณจราจรและผู้โดยสารในอนาคต',
        'consulting_task_01_description': 'จัดทำสถานการณ์ตามปีเป้าหมายและระยะการเติบโตจากผลคาดการณ์และข้อมูลดำเนินงานที่มี '
                                          'เพื่อประเมินความต้องการด้านสิ่งอำนวยความสะดวกและการดำเนินงาน',
        'consulting_task_02_title': 'อุปสงค์ของวันออกแบบและชั่วโมงสูงสุด',
        'consulting_task_02_description': 'แปลงอุปสงค์รายปีเป็นรูปแบบรายวันตัวแทน วันสูงสุด และรายชั่วโมง '
                                          'เพื่อกำหนดปริมาณที่สิ่งอำนวยความสะดวกต้องรองรับ',
        'consulting_task_03_title': 'การจัดทำตารางบินในอนาคต',
        'consulting_task_03_description': 'จัดทำตารางบินสำหรับวันออกแบบจากอุปสงค์ สัดส่วนฝูงบิน รูปแบบสายการบิน และเวลาเปิดดำเนินงาน '
                                          'แล้วประเมินความเป็นไปได้ในการปฏิบัติจริง',
        'consulting_task_04_title': 'สัดส่วนฝูงบินและรูปแบบสายการบิน',
        'consulting_task_04_description': 'เปรียบเทียบผลของขนาดอากาศยาน สัดส่วนสายการบินและเส้นทาง และกลุ่มเที่ยวบินขาเข้า–ขาออก '
                                          'ต่อความต้องการประตูขึ้นเครื่อง หลุมจอด และอาคารผู้โดยสาร',
        'consulting_task_05_title': 'กลุ่มผู้โดยสารและรูปแบบเวลามาถึง',
        'consulting_task_05_description': 'จำลองเวลาและจุดที่ผู้โดยสารขาออก ขาเข้า และเปลี่ยนเครื่องมาถึงสิ่งอำนวยความสะดวก '
                                          'โดยคำนึงถึงรูปแบบเวลามาถึงและการจัดสรรประตูขึ้นเครื่อง',
        'consulting_task_06_title': 'ช่องว่างขีดความสามารถและเกณฑ์เริ่มขยาย',
        'consulting_task_06_description': 'ทดสอบอุปสงค์ที่เพิ่มขึ้นเทียบกับขีดจำกัดและความสามารถรองรับที่เหลือ เพื่อเสนอเกณฑ์เริ่มขยาย '
                                          'ช่วงเวลาเบื้องต้น และลำดับความสำคัญของสิ่งอำนวยความสะดวก',
        'consulting_tab_terminal': 'อาคารผู้โดยสารและเขตนอกการบิน',
        'consulting_terminal_intro': 'ประเมินกระบวนการบริการผู้โดยสาร ผังสิ่งอำนวยความสะดวก การย้ายสายการบิน ระยะก่อสร้าง '
                                     'และการจัดการการเข้าถึง',
        'consulting_task_07_title': 'ขนาดและความเพียงพอของสิ่งอำนวยความสะดวกในอาคารผู้โดยสาร',
        'consulting_task_07_description': 'ประเมินจุดให้บริการและพื้นที่รอเทียบกับอุปสงค์และเกณฑ์บริการ '
                                          'เพื่อระบุจำนวนสิ่งอำนวยความสะดวกและเวลาเปิดใช้งานที่ต้องการ',
        'consulting_task_08_title': 'กระบวนการขาออกและแผนดำเนินงาน',
        'consulting_task_08_description': 'เปรียบเทียบการเปิดใช้ เวลาให้บริการ และกำลังคนของจุดเช็กอิน จุดฝากกระเป๋าด้วยตนเอง '
                                          'จุดตรวจบัตรขึ้นเครื่อง จุดตรวจความปลอดภัย และตรวจคนเข้าเมืองขาออก',
        'consulting_task_09_title': 'ขาเข้า การรับสัมภาระ และศุลกากร',
        'consulting_task_09_description': 'จำลองตรวจคนเข้าเมืองขาเข้า การรับสัมภาระ และศุลกากรร่วมกัน '
                                          'เพื่อประเมินว่าการเปลี่ยนแปลงขั้นตอนหนึ่งส่งผลต่อเวลารวมและความแออัดในขั้นตอนถัดไปอย่างไร',
        'consulting_task_10_title': 'เส้นทางเปลี่ยนเครื่องและการเชื่อมอาคารผู้โดยสาร',
        'consulting_task_10_description': 'ประเมินจุดตรวจความปลอดภัยสำหรับผู้โดยสารเปลี่ยนเครื่อง การเดินทางระหว่างประตู ทางเดิน '
                                          'และชานชาลาระบบขนส่งระหว่างอาคาร ในด้านความแออัดและเวลาเชื่อมต่อเที่ยวบิน',
        'consulting_task_11_title': 'การย้ายสายการบินและผลต่อสิ่งอำนวยความสะดวก',
        'consulting_task_11_description': 'เปรียบเทียบการย้ายสายการบินระหว่างอาคารผู้โดยสาร อาคารเทียบเครื่องบิน โซนเช็กอิน '
                                          'หรือประตูขึ้นเครื่อง ในด้านการกระจายผู้โดยสาร ภาระจุดบริการ เส้นทางเปลี่ยนเครื่อง '
                                          'และความแออัดในพื้นที่รอขึ้นเครื่อง',
        'consulting_task_12_title': 'อาคารผู้โดยสารใหม่และการขยายเป็นระยะ',
        'consulting_task_12_description': 'เปรียบเทียบขนาด ผัง บทบาท และการเชื่อมต่อกับอาคารเดิม '
                                          'เพื่อประเมินขีดความสามารถในวันเปิดใช้และระยะขยายถัดไป',
        'consulting_task_13_title': 'การปรับปรุงท่าอากาศยานขณะเปิดดำเนินงาน',
        'consulting_task_13_description': 'ประเมินการปิดพื้นที่และการลดจำนวนสิ่งอำนวยความสะดวกที่ใช้งานได้ '
                                          'เพื่อกำหนดชุดการปิดที่ทำได้จริงและรูปแบบดำเนินงานชั่วคราว',
        'consulting_task_14_title': 'การสัญจรของผู้โดยสารและผังคิว',
        'consulting_task_14_description': 'เปรียบเทียบความกว้างทางเดิน ฉากกั้น ทางเบี่ยง และผังคิว ในด้านระยะเดิน ความแออัด และเวลาพำนัก '
                                          'แล้วเสนอการปรับพื้นที่',
        'consulting_task_15_title': 'การเข้าถึงเขตนอกการบินและจุดเชื่อมต่อขนส่ง',
        'consulting_task_15_description': 'ประเมินการมาถึงของผู้โดยสารและยานพาหนะ พร้อมทางเลือกผังจุดรับส่งหน้าอาคาร ที่จอดรถ ถนนเข้าออก '
                                          'และจุดเชื่อมต่อขนส่งสาธารณะ ภายในขอบเขตที่ตกลง',
        'consulting_task_16_title': 'เงื่อนไขร่วมและสถานการณ์กดดัน',
        'consulting_task_16_description': 'รวมอุปสงค์สูงสุด เที่ยวบินล่าช้า การปิดพื้นที่ และการย้ายสายการบิน '
                                          'เพื่อระบุจุดเปราะบางและเปรียบเทียบทางเลือกบรรเทาความแออัดและฟื้นฟูการดำเนินงาน',
        'consulting_tab_airside': 'เขตการบิน',
        'consulting_airside_intro': 'ประเมินแผนทางวิ่ง ทางขับ หลุมจอด และสิ่งอำนวยความสะดวกสนับสนุน '
                                    'ควบคู่กับการปฏิบัติการอากาศยานและบริการภาคพื้น',
        'consulting_task_17_title': 'ขีดความสามารถทางวิ่งและความล่าช้าเที่ยวบิน',
        'consulting_task_17_description': 'จำลองรูปแบบปฏิบัติการ เวลาครองทางวิ่ง ระยะห่าง และการจราจรหนาแน่น '
                                          'เพื่อประเมินอัตรารองรับเที่ยวบินและความล่าช้าขาเข้า–ขาออก รวมถึงภาวะทัศนวิสัยต่ำ',
        'consulting_task_18_title': 'ตำแหน่งและผังทางขับออกด่วน',
        'consulting_task_18_description': 'เปรียบเทียบตำแหน่งและระยะห่างของทางขับออกด่วน '
                                          'โดยพิจารณาลักษณะการลงจอดของอากาศยานและเวลาครองทางวิ่ง',
        'consulting_task_19_title': 'การปรับผังเขตการบินและผลกระทบ',
        'consulting_task_19_description': 'ประเมินผลของการสร้าง ขยาย เชื่อมต่อใหม่ หรือปิดทางวิ่ง ทางขับ และลานจอด ต่อเส้นทาง '
                                          'เวลาขับเคลื่อน คอขวด และการรบกวนการปฏิบัติการ',
        'consulting_task_20_title': 'การจัดสรรหลุมจอดและการดันถอยพร้อมกัน',
        'consulting_task_20_description': 'ประเมินความเข้ากันได้ของอากาศยาน การจัดสรรหลุมจอดประชิดอาคารและระยะไกล การครองหลุมจอด '
                                          'และการเคลื่อนที่พร้อมกัน เพื่อเสนอทางเลือกผังและการปฏิบัติการ',
        'consulting_task_21_title': 'การเคลื่อนที่ของอากาศยานและรถบริการภาคพื้น',
        'consulting_task_21_description': 'จำลองการเคลื่อนที่และดันถอยของอากาศยานร่วมกับงานและเส้นทางของยานพาหนะ '
                                          'เพื่อประเมินความแออัดบนถนนบริการ การรบกวนบริเวณทางข้าม และแผนเดินรถ',
        'consulting_task_22_title': 'ลานจอดสินค้าและการปฏิบัติการอากาศยานขนส่งสินค้า',
        'consulting_task_22_description': 'ประเมินความเข้ากันได้ของหลุมจอดสำหรับอากาศยานขนส่งสินค้าขนาดใหญ่ การครองหลุมจอด เส้นทางเข้าออก '
                                          'และการเชื่อมต่อกับอาคารสินค้าและโลจิสติกส์ภาคพื้น',
        'consulting_task_23_title': 'การเข้าถึง MRO โรงเก็บอากาศยาน และ GA/FBO',
        'consulting_task_23_description': 'ทบทวนความเข้ากันได้ของอากาศยาน ทางเข้าโรงเก็บ เส้นทางลากจูง '
                                          'และปฏิสัมพันธ์กับลานจอดและถนนบริการข้างเคียง',
        'consulting_task_24_title': 'ผังและการดำเนินงานลานขจัดน้ำแข็ง',
        'consulting_task_24_description': 'ประเมินจำนวนอากาศยานที่รองรับพร้อมกัน เส้นทางเข้าออก และระยะปลอดภัย '
                                          'แล้วเปรียบเทียบคิวและความล่าช้าขาออกภายใต้ระยะเวลาดำเนินการที่แตกต่างกัน',
        'consulting_task_25_title': 'ที่ตั้ง ARFF เชื้อเพลิง และสิ่งอำนวยความสะดวกสนับสนุน',
        'consulting_task_25_description': 'ประเมินที่ตั้งหน่วยกู้ภัยและดับเพลิง ระบบเชื้อเพลิงและสาธารณูปโภค เส้นทางเข้าถึง '
                                          'และพื้นที่บริการ เพื่อประกอบการตัดสินใจด้านผังและการดำเนินงาน',
        'consulting_task_26_title': 'ทัศนวิสัยหอบังคับการบินและข้อจำกัดสิ่งกีดขวาง',
        'consulting_task_26_description': 'เปรียบเทียบแนวการมองเห็นและจุดอับ '
                                          'พร้อมทบทวนการซ้อนทับพื้นผิวจำกัดสิ่งกีดขวางที่เกี่ยวกับแผนทางวิ่งและสิ่งอำนวยความสะดวกโดยรอบในขั้นวางแผน',
        'consulting_tab_digital': 'ดิจิทัลทวิน',
        'consulting_digital_intro': 'จำลองระยะการพัฒนาท่าอากาศยาน ตรวจสอบกฎปฏิบัติการ และพัฒนาความสามารถวิเคราะห์ที่โครงการต้องการ',
        'consulting_task_27_title': 'แบบจำลองท่าอากาศยานปัจจุบันและอนาคต',
        'consulting_task_27_description': 'จัดเตรียมข้อมูลเชิงพื้นที่และจำลองผังปัจจุบัน วันเปิดใช้ การขยายระหว่างทาง '
                                          'และผังพัฒนาเต็มรูปแบบ พร้อมสิ่งอำนวยความสะดวกที่วางแผนไว้ในแต่ละระยะ',
        'consulting_task_28_title': 'แบบจำลองเฉพาะท่าอากาศยานและการตรวจสอบการปฏิบัติการ',
        'consulting_task_28_description': 'กำหนดผัง กฎใช้สิ่งอำนวยความสะดวก และขั้นตอนปฏิบัติการเฉพาะ '
                                          'แล้วตรวจสอบและปรับเทียบกับข้อมูลสังเกตและบันทึกการดำเนินงานที่มี',
        'consulting_task_29_title': 'การซ้อนทับแบบและภาพจำลองเชิงพื้นที่',
        'consulting_task_29_description': 'เปรียบเทียบแบบเดิม ทางเลือก และระยะก่อสร้าง พร้อมอธิบายการไหลของอากาศยาน ยานพาหนะ '
                                          'และผู้โดยสารผ่านผัง แบบจำลองเชิงพื้นที่ และวิดีโอจำลอง',
        'consulting_task_30_title': 'KPI และฟังก์ชันวิเคราะห์เฉพาะ',
        'consulting_task_30_description': 'กำหนดตัวชี้วัดเฉพาะท่าอากาศยาน เช่น '
                                          'การใช้งานประตูขึ้นเครื่องพร้อมกันและการใช้เวลาเปลี่ยนเครื่องเกินเกณฑ์ พร้อมจัดเตรียมข้อมูลเข้า '
                                          'ผลลัพธ์ และฟังก์ชันเข้าถึงผลที่ต้องการ',
        'consulting_scope_note': 'ขอบเขต ระดับรายละเอียดแบบจำลอง และเกณฑ์ประเมินจะตกลงตามข้อมูลท่าอากาศยาน เงื่อนไขดำเนินงาน '
                                 'และข้อกำหนดโครงการ ส่วนการศึกษาเพิ่มเติม การพัฒนาฟังก์ชัน '
                                 'และการเชื่อมระบบภายนอกจะกำหนดขอบเขตพร้อมระยะเวลาที่จำเป็น',
        'consulting_expertise_heading': 'เทคโนโลยีและประสบการณ์ท่าอากาศยาน',
        'consulting_expertise_origin': 'Team Flexa มีจุดเริ่มต้นจากโครงการธุรกิจภายในของ Incheon International Airport Corporation '
                                       'ทีมงานมีประสบการณ์ปรับปรุงการดำเนินงานและขยายท่าอากาศยานอินชอน '
                                       'รวมถึงงานในธุรกิจท่าอากาศยานต่างประเทศขององค์กร',
        'consulting_expertise_01_title': 'ซอฟต์แวร์ที่พัฒนาเอง',
        'consulting_expertise_01_description': 'เราพัฒนาและเป็นเจ้าของซอฟต์แวร์ จึงปรับแบบจำลองและฟังก์ชันให้เหมาะกับการศึกษา '
                                               'พร้อมลดความจำเป็นในการใช้เครื่องมือวิเคราะห์หรือบุคลากรเฉพาะทางแยกต่างหาก',
        'consulting_expertise_02_title': 'KPI และฟังก์ชันวิเคราะห์เฉพาะ',
        'consulting_expertise_02_description': 'เราใช้ตัวชี้วัด เกณฑ์ประเมิน และรูปแบบรายงานของคุณ '
                                               'พร้อมตกลงการพัฒนาหรือเชื่อมระบบเพิ่มเติมเมื่อฟังก์ชันที่มีไม่เพียงพอ',
        'consulting_expertise_03_title': 'กฎและผังเฉพาะท่าอากาศยาน',
        'consulting_expertise_03_description': 'เราจำลองการเชื่อมอาคารผู้โดยสาร กฎใช้สิ่งอำนวยความสะดวกของสายการบิน รูปแบบหลุมจอด '
                                               'เส้นทางบริการภาคพื้น และข้อจำกัดตามช่วงเวลา',
        'consulting_expertise_04_title': 'ข้อมูลและแบบจำลองที่มีอยู่',
        'consulting_expertise_04_description': 'เราใช้ข้อมูลท่าอากาศยาน เที่ยวบิน สิ่งอำนวยความสะดวก และแบบจำลองที่มี เพื่อลดเวลาเตรียมงาน '
                                               'พร้อมตรวจสอบกับข้อมูลสังเกตของคุณและเกณฑ์ที่ตกลง',
        'consulting_expertise_05_title': 'การเชื่อมโยงการไหลของอากาศยาน ยานพาหนะ และผู้โดยสาร',
        'consulting_expertise_05_description': 'จำลองการเคลื่อนที่ของอากาศยานร่วมกับงานยานพาหนะ '
                                               'และเชื่อมการศึกษาเขตการบินกับอาคารผู้โดยสารผ่านการจัดสรรประตูและเวลามาถึงของผู้โดยสาร '
                                               'เพื่อประเมินผลกระทบในภาพรวมของการเปลี่ยนสิ่งอำนวยความสะดวก',
        'consulting_engagements_heading': 'รูปแบบการทำงานร่วมกัน',
        'consulting_engagements_terms': 'เลือกใช้บริการที่ปรึกษาอย่างเดียว '
                                        'หรือบริการที่ปรึกษาร่วมกับฟังก์ชันหรือสิทธิ์ใช้ซอฟต์แวร์ที่เลือกได้ การเข้าถึงผลโดยตรง '
                                        'ฟังก์ชันทบทวนต่อเนื่อง และเงื่อนไขการใช้จะตกลงแยกต่างหาก',
        'consulting_engagements_01_title': 'ที่ปรึกษารายโครงการ',
        'consulting_engagements_01_application': 'การขยายท่าอากาศยาน การย้ายสายการบิน แผนก่อสร้าง และความต้องการวางแผนอื่นที่กำหนดชัดเจน',
        'consulting_engagements_01_role': 'เราพัฒนาแบบจำลอง เปรียบเทียบทางเลือก และเสนอการปรับปรุง '
                                          'พร้อมจัดทำผลสำหรับการพิจารณาแผนและงบประมาณ',
        'consulting_engagements_02_title': 'ข้อเสนอร่วมและการดำเนินโครงการ',
        'consulting_engagements_02_application': 'การจำลองและประเมินขีดความสามารถในงานออกแบบ วิศวกรรม และที่ปรึกษา',
        'consulting_engagements_02_role': 'ในขั้นเสนอราคา เราตกลงวิธีการ หน้าที่ แผนงาน และค่าบริการ '
                                          'เมื่อได้รับงานจึงดำเนินการวิเคราะห์ตามที่ตกลงเพื่อทดสอบแบบและเปรียบเทียบทางเลือก',
        'consulting_engagements_03_title': 'พันธมิตรทางเทคนิคต่อเนื่อง',
        'consulting_engagements_03_application': 'การวิเคราะห์เฉพาะทางสำหรับโครงการท่าอากาศยานหลายโครงการ',
        'consulting_engagements_03_role': 'เราสนับสนุนการทบทวนแบบ วิเคราะห์สถานการณ์ และให้คำปรึกษาทางเทคนิคตามระยะเวลาที่ตกลง '
                                          'โดยไม่ต้องจัดตั้งทีมวิเคราะห์ภายในโดยเฉพาะ',
        'consulting_deliverables_heading': 'ผลงานส่งมอบ',
        'consulting_deliverables_usage_rights': 'สิทธิ์และระยะเวลาใช้ข้อมูล แบบจำลอง บัญชี '
                                                'หรือฟังก์ชันโซลูชันที่ส่งมอบจะกำหนดตามงานที่ว่าจ้าง',
        'consulting_deliverables_01_title': 'รายงานที่ปรึกษา',
        'consulting_deliverables_01_use': 'รายงานทางเทคนิคหรือบทสรุปผู้บริหาร ครอบคลุมวัตถุประสงค์ ผลประเมินทางเลือก ข้อเสนอแนะ '
                                          'และลำดับความสำคัญการลงทุน',
        'consulting_deliverables_02_title': 'รายงานเว็บ HTML',
        'consulting_deliverables_02_use': 'ทบทวนสถานการณ์ ผลเปรียบเทียบ และภาพเชิงพื้นที่ผ่านเบราว์เซอร์',
        'consulting_deliverables_03_title': 'PDF และ DOCX',
        'consulting_deliverables_03_use': 'สำหรับส่งโครงการ ทบทวนภายใน แก้ไขร่วมกัน และเผยแพร่ฉบับพิมพ์',
        'consulting_deliverables_04_title': 'วิดีโอและภาพเรนเดอร์',
        'consulting_deliverables_04_use': 'วิดีโอจำลอง ภาพเปรียบเทียบผังทางเลือก '
                                          'และภาพเชิงพื้นที่สำหรับการประชุมและสื่อสารกับผู้มีส่วนได้ส่วนเสีย',
        'consulting_deliverables_05_title': 'ข้อมูล แบบจำลอง และองค์ประกอบโซลูชันที่เลือก',
        'consulting_deliverables_05_use': 'ชุดข้อมูล แพ็กเกจแบบจำลอง บัญชีเข้าถึง หรือฟังก์ชันที่ส่งมอบตามข้อตกลงการว่าจ้าง',
        'consulting_programme_heading': 'แผนงานและค่าบริการ',
        'consulting_programme_01_title': 'แผนงานตามโครงการ',
        'consulting_programme_01_description': 'เราจัดแผนงานให้สอดคล้องกับกำหนดการโครงการ โดยคำนึงถึงขอบเขตศึกษา การเตรียมข้อมูล '
                                               'การตรวจสอบแบบจำลอง และรอบทบทวน',
        'consulting_programme_02_title': 'การสนับสนุนตามระยะเวลา',
        'consulting_programme_02_description': 'ให้บริการทบทวนแบบ วิเคราะห์สถานการณ์ และคำปรึกษาทางเทคนิคตามระยะเวลาที่ตกลง เช่น หนึ่ง สาม '
                                               'หรือหกเดือน โดยตกลงปริมาณงาน ความถี่ และเวลาตอบกลับแยกต่างหาก',
        'consulting_programme_03_title': 'การส่งมอบเป็นระยะ',
        'consulting_programme_03_description': 'ว่าจ้างศึกษาในขั้นแนวคิด ออกแบบเบื้องต้น ออกแบบรายละเอียด และก่อสร้าง '
                                               'พร้อมทบทวนเพิ่มเติมเมื่อแผนเปลี่ยน',
        'consulting_programme_04_title': 'ค่าบริการ',
        'consulting_programme_04_description': 'ค่าบริการพิจารณาจากขอบเขต ขนาดโครงการ ระยะเวลา จำนวนทางเลือก และความต้องการพัฒนาเฉพาะ',
        'footer_copyright': 'ลิขสิทธิ์ 2026 TeamFlexa CO., LTD. สงวนลิขสิทธิ์',
        'flexa_about_title': 'รู้จัก Flexa',
        'flexa_about_p1': 'Flexa เป็นแบรนด์ของ TeamFlexa CO., LTD. '
                          'บริษัทผู้เชี่ยวชาญด้านโซลูชันสนามบินที่ใช้ข้อมูลทำความเข้าใจความซับซ้อนของการดำเนินงานสนามบิน '
                          'และใช้เทคโนโลยีการจำลองกับการวิเคราะห์ด้วย AI เพื่อให้ได้ผลลัพธ์ที่เหมาะสมที่สุด '
                          'เราต่อยอดจากการวิเคราะห์เป็นข้อเสนอที่นำไปปฏิบัติได้ เพื่อปรับปรุงการดำเนินงานอย่างเป็นรูปธรรม',
        'flexa_about_p2': 'TeamFlexa เริ่มต้นจากโครงการธุรกิจภายในของท่าอากาศยานนานาชาติอินชอน '
                          'โดยนำประสบการณ์และข้อมูลจากสภาพแวดล้อมสนามบินชั้นนำของโลกมาใช้ '
                          'เราให้บริการที่ปรึกษาและโซลูชันอย่างครบวงจรภายใต้แบรนด์ Flexa '
                          'ตั้งแต่การเพิ่มประสิทธิภาพการดำเนินงานอาคารผู้โดยสารไปจนถึงกลยุทธ์โครงสร้างพื้นฐานระยะกลางและระยะยาว '
                          'เพื่อช่วยให้ลูกค้ากำหนดปัญหาที่ซับซ้อนในเชิงปริมาณและตัดสินใจได้อย่างมีประสิทธิผลสูงสุด',
        'flexa_about_p3': 'TeamFlexa ให้บริการสนามบิน ผู้ดำเนินงานสนามบิน และบริษัทวิศวกรรมและก่อสร้างทั่วโลก '
                          'โดยวิเคราะห์ปัญหาอย่างรวดเร็วและแม่นยำ ออกแบบกลยุทธ์ให้เหมาะกับแต่ละโครงการ และดูแลให้เกิดการนำไปปฏิบัติ '
                          'เรากำหนดมาตรฐานใหม่ให้การดำเนินงานสนามบิน และเป็นพันธมิตรชั้นนำด้านการตัดสินใจบนพื้นฐานข้อมูลในตลาดโลก'},
 'vi': {'consulting_eyebrow': 'Dịch vụ tư vấn',
        'consulting_heading': 'Tư vấn sân bay',
        'consulting_intro': 'Quy hoạch, mô phỏng và hỗ trợ kỹ thuật cho sân bay và các nhóm kỹ thuật.',
        'consulting_projects_heading': 'Ứng dụng trong dự án',
        'consulting_tab_overall': 'Tổng quan',
        'consulting_tabs_aria': 'Các lĩnh vực tư vấn',
        'consulting_overall_intro': 'Các dự án điển hình gồm sân bay và nhà ga mới, mở rộng, cải tạo trong khi vẫn khai thác, di dời hãng '
                                    'hàng không hoặc cơ sở, đầu tư theo giai đoạn và cải thiện vận hành.',
        'consulting_overall_01_title': 'Di dời hãng hàng không',
        'consulting_overall_01_role': 'Đánh giá khả năng tiếp nhận hãng hàng không chuyển đến của khu làm thủ tục, kiểm tra an ninh và nối '
                                      'chuyến; so sánh các phương án bố trí phù hợp.',
        'consulting_overall_02_title': 'Nhà ga mới và mở rộng sân bay',
        'consulting_overall_02_role': 'So sánh thời điểm khai trương, quy mô cơ sở và phân chia chức năng giữa nhà ga mới với nhà ga hiện '
                                      'hữu.',
        'consulting_overall_03_title': 'Thay đổi mặt bằng khu bay',
        'consulting_overall_03_role': 'Đánh giá ảnh hưởng của đường lăn và vị trí đỗ điều chỉnh đến chuyển động tàu bay và luồng xe phục '
                                      'vụ mặt đất.',
        'consulting_overall_04_title': 'Cải tạo trong khi vẫn khai thác',
        'consulting_overall_04_role': 'Đánh giá những cơ sở có thể đóng đồng thời, đồng thời so sánh tuyến tạm và trình tự thi công.',
        'consulting_overall_05_title': 'Đề xuất thiết kế và kỹ thuật liên danh',
        'consulting_overall_05_role': 'Tham gia đề xuất với vai trò đối tác kỹ thuật về mô phỏng và đánh giá năng lực, sau đó thực hiện '
                                      'phân tích đã thống nhất khi trúng thầu.',
        'consulting_overall_06_title': 'Chiến lược phát triển sân bay',
        'consulting_overall_06_role': 'Đánh giá nhu cầu, năng lực và các phương án để hỗ trợ xác định thời điểm đầu tư và quy mô cơ sở.',
        'consulting_tab_demand': 'Nhu cầu & Lịch bay',
        'consulting_demand_intro': 'Chuyển nhu cầu tương lai thành kịch bản khai thác, yêu cầu cơ sở và cơ sở quyết định mở rộng.',
        'consulting_task_01_title': 'Nhu cầu giao thông và hành khách tương lai',
        'consulting_task_01_description': 'Xây dựng kịch bản theo năm mục tiêu và giai đoạn tăng trưởng từ dự báo, dữ liệu khai thác hiện '
                                          'có để đánh giá yêu cầu về cơ sở và vận hành.',
        'consulting_task_02_title': 'Nhu cầu ngày thiết kế và giờ cao điểm',
        'consulting_task_02_description': 'Chuyển nhu cầu hằng năm thành biểu đồ ngày đại diện, ngày cao điểm và theo giờ để xác định tải '
                                          'mà cơ sở cần đáp ứng.',
        'consulting_task_03_title': 'Xây dựng lịch bay tương lai',
        'consulting_task_03_description': 'Xây dựng lịch bay ngày thiết kế từ nhu cầu, cơ cấu đội bay, đặc điểm hãng hàng không và giờ '
                                          'hoạt động; đánh giá tính khả thi trong khai thác.',
        'consulting_task_04_title': 'Cơ cấu đội bay và đặc điểm hãng hàng không',
        'consulting_task_04_description': 'So sánh tác động của kích thước tàu bay, cơ cấu hãng và đường bay, cùng các đợt chuyến bay đến '
                                          'và đi đối với nhu cầu cửa ra tàu bay, vị trí đỗ và nhà ga.',
        'consulting_task_05_title': 'Nhóm hành khách và phân bố thời điểm đến',
        'consulting_task_05_description': 'Mô hình hóa thời điểm và nơi hành khách đi, đến và nối chuyến tiếp cận các cơ sở, có xét thời '
                                          'điểm hành khách có mặt và phân bổ cửa ra tàu bay.',
        'consulting_task_06_title': 'Thiếu hụt năng lực và ngưỡng mở rộng',
        'consulting_task_06_description': 'Kiểm tra nhu cầu tăng so với giới hạn và năng lực dự phòng để đề xuất ngưỡng mở rộng, thời điểm '
                                          'dự kiến và thứ tự ưu tiên cơ sở.',
        'consulting_tab_terminal': 'Nhà ga & Khu công cộng',
        'consulting_terminal_intro': 'Đánh giá quy trình phục vụ hành khách, bố trí cơ sở, di dời hãng hàng không, phân kỳ thi công và '
                                     'phương án tiếp cận.',
        'consulting_task_07_title': 'Quy mô và mức đáp ứng của cơ sở nhà ga',
        'consulting_task_07_description': 'Đánh giá các điểm xử lý và khu chờ theo nhu cầu, tiêu chí dịch vụ để xác định số lượng cơ sở và '
                                          'giờ hoạt động cần thiết.',
        'consulting_task_08_title': 'Quy trình hành khách đi và kế hoạch vận hành',
        'consulting_task_08_description': 'So sánh việc mở điểm phục vụ, giờ hoạt động và bố trí nhân sự tại quầy làm thủ tục, gửi hành lý '
                                          'tự động, kiểm tra thẻ lên tàu bay, an ninh và xuất cảnh.',
        'consulting_task_09_title': 'Hành khách đến, nhận hành lý và hải quan',
        'consulting_task_09_description': 'Mô hình hóa đồng thời nhập cảnh, nhận hành lý và hải quan để đánh giá tác động của thay đổi tại '
                                          'một bước đến tổng thời gian xử lý và ùn tắc ở bước sau.',
        'consulting_task_10_title': 'Luồng nối chuyến và kết nối nhà ga',
        'consulting_task_10_description': 'Đánh giá an ninh nối chuyến, di chuyển giữa các cửa, hành lang và sân ga của hệ thống vận '
                                          'chuyển liên nhà ga về ùn tắc và thời gian nối chuyến.',
        'consulting_task_11_title': 'Di dời hãng hàng không và tác động đến cơ sở',
        'consulting_task_11_description': 'So sánh việc chuyển hãng giữa các nhà ga, khu cửa ra tàu bay, khu làm thủ tục hoặc cửa về phân '
                                          'bố hành khách, tải cơ sở, tuyến nối chuyến và ùn tắc phòng chờ.',
        'consulting_task_12_title': 'Nhà ga mới và mở rộng theo giai đoạn',
        'consulting_task_12_description': 'So sánh quy mô, bố trí, chức năng và kết nối với nhà ga hiện hữu để đánh giá năng lực khi khai '
                                          'trương và ở các giai đoạn mở rộng tiếp theo.',
        'consulting_task_13_title': 'Cải tạo khi sân bay vẫn khai thác',
        'consulting_task_13_description': 'Đánh giá việc đóng và giảm khả năng sử dụng cơ sở để xác định các tổ hợp đóng khả thi và phương '
                                          'án vận hành tạm thời.',
        'consulting_task_14_title': 'Lưu thông hành khách và bố trí hàng chờ',
        'consulting_task_14_description': 'So sánh chiều rộng hành lang, vách ngăn, tuyến chuyển hướng và bố trí hàng chờ về quãng đường '
                                          'đi bộ, ùn tắc và thời gian lưu lại; đề xuất cải thiện không gian.',
        'consulting_task_15_title': 'Tiếp cận khu công cộng và kết nối giao thông',
        'consulting_task_15_description': 'Đánh giá lượng hành khách, phương tiện đến và các phương án bố trí điểm đón trả, bãi đỗ xe, '
                                          'đường tiếp cận, điểm kết nối giao thông công cộng trong phạm vi thống nhất.',
        'consulting_task_16_title': 'Điều kiện kết hợp và kịch bản áp lực cao',
        'consulting_task_16_description': 'Kết hợp nhu cầu cao điểm, chuyến bay chậm, đóng cơ sở và di dời hãng để xác định điểm dễ quá '
                                          'tải, so sánh phương án giảm ùn tắc và khôi phục vận hành.',
        'consulting_tab_airside': 'Khu bay',
        'consulting_airside_intro': 'Đánh giá phương án đường cất hạ cánh, đường lăn, vị trí đỗ và cơ sở hỗ trợ cùng với hoạt động tàu bay '
                                    'và phục vụ mặt đất.',
        'consulting_task_17_title': 'Năng lực đường cất hạ cánh và chậm chuyến',
        'consulting_task_17_description': 'Mô hình hóa phương thức khai thác, thời gian chiếm dụng, phân cách và lưu lượng tập trung để '
                                          'đánh giá năng lực thông qua, chậm chuyến đến và đi, kể cả trong điều kiện tầm nhìn thấp.',
        'consulting_task_18_title': 'Vị trí và bố trí đường lăn thoát nhanh',
        'consulting_task_18_description': 'So sánh vị trí, khoảng cách đường lăn thoát nhanh theo đặc tính hạ cánh của tàu bay và thời '
                                          'gian chiếm dụng đường cất hạ cánh.',
        'consulting_task_19_title': 'Thay đổi mặt bằng khu bay và tác động',
        'consulting_task_19_description': 'Đánh giá tác động của đường cất hạ cánh, đường lăn và sân đỗ mới, mở rộng, nối lại hoặc đóng '
                                          'đến tuyến di chuyển, thời gian lăn, điểm nghẽn và xung đột khai thác.',
        'consulting_task_20_title': 'Phân bổ vị trí đỗ và đẩy lùi đồng thời',
        'consulting_task_20_description': 'Đánh giá khả năng phù hợp với tàu bay, phân bổ vị trí đỗ tiếp xúc và đỗ xa, chiếm dụng và '
                                          'chuyển động đồng thời để đề xuất phương án bố trí, khai thác.',
        'consulting_task_21_title': 'Chuyển động tàu bay và xe phục vụ mặt đất',
        'consulting_task_21_description': 'Mô hình hóa tàu bay di chuyển và đẩy lùi cùng nhiệm vụ, tuyến xe để đánh giá ùn tắc đường công '
                                          'vụ, xung đột tại giao cắt và kế hoạch vận hành phương tiện.',
        'consulting_task_22_title': 'Sân đỗ hàng hóa và khai thác tàu bay chở hàng',
        'consulting_task_22_description': 'Đánh giá vị trí đỗ phù hợp với tàu bay chở hàng lớn, thời gian chiếm dụng, tuyến tiếp cận và '
                                          'kết nối với nhà ga hàng hóa, logistics mặt đất.',
        'consulting_task_23_title': 'Tiếp cận MRO, hangar và GA/FBO',
        'consulting_task_23_description': 'Xem xét sự phù hợp với tàu bay, lối vào hangar, tuyến kéo và tương tác với sân đỗ, đường công '
                                          'vụ lân cận.',
        'consulting_task_24_title': 'Bố trí và vận hành khu khử băng',
        'consulting_task_24_description': 'Đánh giá số tàu bay phục vụ đồng thời, tuyến vào ra và khoảng hở an toàn; so sánh hàng chờ, '
                                          'chậm khởi hành khi thời gian xử lý thay đổi.',
        'consulting_task_25_title': 'Vị trí ARFF, nhiên liệu và cơ sở hỗ trợ',
        'consulting_task_25_description': 'Đánh giá vị trí cơ sở cứu nạn chữa cháy, nhiên liệu, hạ tầng kỹ thuật, tuyến tiếp cận và phạm '
                                          'vi phục vụ để hỗ trợ quyết định bố trí, vận hành.',
        'consulting_task_26_title': 'Tầm nhìn đài kiểm soát và giới hạn chướng ngại vật',
        'consulting_task_26_description': 'So sánh đường ngắm, điểm mù và xem xét phần giao chồng của bề mặt giới hạn chướng ngại vật liên '
                                          'quan đến phương án đường cất hạ cánh, cơ sở xung quanh ở giai đoạn quy hoạch.',
        'consulting_tab_digital': 'Bản sao số',
        'consulting_digital_intro': 'Mô hình hóa các giai đoạn phát triển sân bay, kiểm chứng quy tắc khai thác và xây dựng năng lực phân '
                                    'tích cần cho dự án.',
        'consulting_task_27_title': 'Mô hình sân bay hiện tại và tương lai',
        'consulting_task_27_description': 'Chuẩn bị dữ liệu không gian, mô hình hóa mặt bằng hiện hữu, khai trương, mở rộng trung gian và '
                                          'hoàn chỉnh, với các cơ sở dự kiến cho từng giai đoạn.',
        'consulting_task_28_title': 'Mô hình riêng cho sân bay và kiểm chứng khai thác',
        'consulting_task_28_description': 'Thiết lập bố trí đặc thù, quy tắc sử dụng cơ sở và quy trình khai thác; kiểm chứng, hiệu chỉnh '
                                          'theo quan sát và hồ sơ khai thác sẵn có.',
        'consulting_task_29_title': 'Chồng lớp thiết kế và trực quan hóa không gian',
        'consulting_task_29_description': 'So sánh phương án hiện hữu, phương án thay thế và giai đoạn thi công; giải thích luồng tàu bay, '
                                          'phương tiện, hành khách bằng mặt bằng, mô hình không gian và video mô phỏng.',
        'consulting_task_30_title': 'KPI và chức năng phân tích tùy chỉnh',
        'consulting_task_30_description': 'Xác định chỉ số riêng của sân bay, gồm khai thác cửa đồng thời và vượt ngưỡng thời gian nối '
                                          'chuyến; cấu hình dữ liệu đầu vào, đầu ra và chức năng truy cập kết quả cần thiết.',
        'consulting_scope_note': 'Phạm vi, mức chi tiết mô hình và tiêu chí đánh giá được thống nhất theo dữ liệu sân bay, điều kiện khai '
                                 'thác và yêu cầu dự án. Nghiên cứu bổ sung, phát triển chức năng và tích hợp hệ thống ngoài được xác định '
                                 'phạm vi cùng tiến độ cần thiết.',
        'consulting_expertise_heading': 'Công nghệ và kinh nghiệm sân bay',
        'consulting_expertise_origin': 'Team Flexa hình thành từ chương trình khởi nghiệp nội bộ của Incheon International Airport '
                                       'Corporation. Đội ngũ đã tham gia cải thiện khai thác, mở rộng sân bay Incheon và các nhiệm vụ '
                                       'thuộc hoạt động sân bay ở nước ngoài của tập đoàn.',
        'consulting_expertise_01_title': 'Phần mềm tự phát triển',
        'consulting_expertise_01_description': 'Chúng tôi phát triển và sở hữu phần mềm, điều chỉnh mô hình và chức năng theo nghiên cứu, '
                                               'đồng thời giảm nhu cầu dùng công cụ phân tích hoặc nhân sự chuyên môn riêng.',
        'consulting_expertise_02_title': 'KPI và chức năng phân tích tùy chỉnh',
        'consulting_expertise_02_description': 'Chúng tôi sử dụng chỉ số hiệu quả, tiêu chí đánh giá và mẫu báo cáo của bạn; thống nhất '
                                               'phát triển hoặc tích hợp bổ sung khi chức năng hiện có chưa đáp ứng.',
        'consulting_expertise_03_title': 'Quy tắc và mặt bằng riêng của sân bay',
        'consulting_expertise_03_description': 'Chúng tôi mô hình hóa kết nối nhà ga, quy tắc sử dụng cơ sở của hãng, cấu hình vị trí đỗ, '
                                               'tuyến phục vụ mặt đất và hạn chế theo thời gian.',
        'consulting_expertise_04_title': 'Dữ liệu và mô hình hiện có',
        'consulting_expertise_04_description': 'Chúng tôi sử dụng dữ liệu sân bay, chuyến bay, cơ sở và mô hình sẵn có để rút ngắn thiết '
                                               'lập, đồng thời kiểm chứng theo quan sát của bạn và tiêu chí đã thống nhất.',
        'consulting_expertise_05_title': 'Liên kết luồng tàu bay, phương tiện và hành khách',
        'consulting_expertise_05_description': 'Chuyển động tàu bay và nhiệm vụ phương tiện được mô hình hóa cùng nhau; phân bổ cửa, thời '
                                               'điểm hành khách đến kết nối nghiên cứu khu bay với nhà ga để đánh giá tác động rộng hơn '
                                               'của thay đổi cơ sở.',
        'consulting_engagements_heading': 'Hợp tác với chúng tôi',
        'consulting_engagements_terms': 'Có thể sử dụng dịch vụ tư vấn riêng hoặc kết hợp các chức năng, giấy phép phần mềm được chọn. '
                                        'Quyền truy cập trực tiếp kết quả, chức năng xem xét tiếp theo và điều khoản sử dụng được thống '
                                        'nhất riêng.',
        'consulting_engagements_01_title': 'Tư vấn theo dự án',
        'consulting_engagements_01_application': 'Mở rộng sân bay, di dời hãng hàng không, kế hoạch thi công và các nhu cầu quy hoạch đã '
                                                 'xác định.',
        'consulting_engagements_01_role': 'Chúng tôi phát triển mô hình, so sánh phương án và đề xuất cải thiện; chuẩn bị kết quả phục vụ '
                                          'xem xét quy hoạch và ngân sách.',
        'consulting_engagements_02_title': 'Đề xuất liên danh và thực hiện dự án',
        'consulting_engagements_02_application': 'Mô phỏng và đánh giá năng lực trong các nhiệm vụ thiết kế, kỹ thuật và tư vấn.',
        'consulting_engagements_02_role': 'Ở giai đoạn đề xuất, chúng tôi thống nhất phương pháp, trách nhiệm, tiến độ và phí; sau khi '
                                          'trúng thầu, thực hiện phân tích đã thống nhất để kiểm tra thiết kế và so sánh phương án.',
        'consulting_engagements_03_title': 'Đối tác kỹ thuật dài hạn',
        'consulting_engagements_03_application': 'Phân tích chuyên sâu cho nhiều dự án sân bay.',
        'consulting_engagements_03_role': 'Chúng tôi cung cấp thẩm tra thiết kế, phân tích kịch bản và tư vấn kỹ thuật trong thời hạn '
                                          'thống nhất, không cần đội phân tích nội bộ chuyên trách.',
        'consulting_deliverables_heading': 'Sản phẩm bàn giao',
        'consulting_deliverables_usage_rights': 'Quyền và thời hạn sử dụng dữ liệu, mô hình, tài khoản hoặc chức năng giải pháp bàn giao '
                                                'được quy định theo hợp đồng.',
        'consulting_deliverables_01_title': 'Báo cáo tư vấn',
        'consulting_deliverables_01_use': 'Báo cáo kỹ thuật hoặc tóm tắt điều hành về mục tiêu, đánh giá phương án, khuyến nghị và ưu tiên '
                                          'đầu tư.',
        'consulting_deliverables_02_title': 'Báo cáo web HTML',
        'consulting_deliverables_02_use': 'Xem kịch bản, so sánh và trực quan hóa không gian trên trình duyệt.',
        'consulting_deliverables_03_title': 'PDF và DOCX',
        'consulting_deliverables_03_use': 'Nộp hồ sơ dự án, xem xét nội bộ, chỉnh sửa cộng tác và phát hành bản in.',
        'consulting_deliverables_04_title': 'Video và hình ảnh kết xuất',
        'consulting_deliverables_04_use': 'Video mô phỏng, so sánh mặt bằng và hình ảnh không gian phục vụ họp, trao đổi với các bên liên '
                                          'quan.',
        'consulting_deliverables_05_title': 'Dữ liệu, mô hình và thành phần giải pháp được chọn',
        'consulting_deliverables_05_use': 'Bộ dữ liệu, gói mô hình, tài khoản truy cập hoặc chức năng được bàn giao theo thỏa thuận.',
        'consulting_programme_heading': 'Tiến độ và phí',
        'consulting_programme_01_title': 'Tiến độ theo dự án',
        'consulting_programme_01_description': 'Chúng tôi điều chỉnh kế hoạch theo tiến độ dự án, có tính đến phạm vi nghiên cứu, chuẩn bị '
                                               'dữ liệu, kiểm chứng mô hình và các đợt xem xét.',
        'consulting_programme_02_title': 'Hỗ trợ theo thời hạn',
        'consulting_programme_02_description': 'Thẩm tra thiết kế, phân tích kịch bản và tư vấn kỹ thuật theo thời hạn thống nhất, như '
                                               'một, ba hoặc sáu tháng; khối lượng, tần suất và thời gian phản hồi được thỏa thuận riêng.',
        'consulting_programme_03_title': 'Bàn giao theo giai đoạn',
        'consulting_programme_03_description': 'Đặt nghiên cứu ở giai đoạn ý tưởng, thiết kế sơ bộ, thiết kế chi tiết và thi công; bổ sung '
                                               'các đợt xem xét khi phương án thay đổi.',
        'consulting_programme_04_title': 'Phí dịch vụ',
        'consulting_programme_04_description': 'Phí được xác định theo phạm vi, quy mô dự án, thời hạn, số phương án và yêu cầu phát triển '
                                               'tùy chỉnh.',
        'footer_copyright': 'Bản quyền 2026 TeamFlexa CO., LTD. Bảo lưu mọi quyền.',
        'flexa_about_title': 'Về Flexa',
        'flexa_about_p1': 'Flexa là thương hiệu của TeamFlexa CO., LTD., công ty chuyên về giải pháp sân bay, sử dụng dữ liệu để làm rõ '
                          'những vấn đề phức tạp trong vận hành sân bay và mang lại kết quả tối ưu thông qua công nghệ mô phỏng và phân '
                          'tích ứng dụng AI. Chúng tôi đi xa hơn việc phân tích, đưa ra những nhận định có thể chuyển thành hành động để '
                          'cải thiện vận hành một cách thực chất.',
        'flexa_about_p2': 'Khởi nguồn từ một dự án khởi nghiệp nội bộ tại Sân bay Quốc tế Incheon, TeamFlexa ứng dụng kinh nghiệm và dữ '
                          'liệu từ một trong những môi trường sân bay hàng đầu thế giới. Dưới thương hiệu Flexa, chúng tôi cung cấp dịch '
                          'vụ tư vấn và giải pháp toàn diện, từ tối ưu hóa vận hành nhà ga đến chiến lược hạ tầng trung và dài hạn, giúp '
                          'khách hàng lượng hóa các thách thức phức tạp và đưa ra quyết định hiệu quả nhất.',
        'flexa_about_p3': 'Phục vụ các sân bay, đơn vị khai thác sân bay và doanh nghiệp kỹ thuật, xây dựng trên toàn cầu, TeamFlexa chẩn '
                          'đoán vấn đề nhanh chóng, chính xác, thiết kế chiến lược phù hợp và bảo đảm triển khai. Chúng tôi định hình lại '
                          'các tiêu chuẩn vận hành sân bay và là đối tác hàng đầu về ra quyết định dựa trên dữ liệu trên thị trường toàn '
                          'cầu.'},
 'id': {'consulting_eyebrow': 'Layanan konsultasi',
        'consulting_heading': 'Konsultasi bandara',
        'consulting_intro': 'Perencanaan, simulasi, dan dukungan teknis untuk bandara dan tim rekayasa.',
        'consulting_projects_heading': 'Penerapan dalam proyek',
        'consulting_tab_overall': 'Gambaran umum',
        'consulting_tabs_aria': 'Bidang layanan konsultasi',
        'consulting_overall_intro': 'Proyek yang umum meliputi bandara dan terminal baru, perluasan, renovasi saat tetap beroperasi, '
                                    'relokasi maskapai atau fasilitas, investasi bertahap, dan peningkatan operasi.',
        'consulting_overall_01_title': 'Relokasi maskapai',
        'consulting_overall_01_role': 'Menilai apakah fasilitas check-in, keamanan, dan transfer dapat menampung maskapai yang direlokasi, '
                                      'serta membandingkan tata letak yang sesuai.',
        'consulting_overall_02_title': 'Terminal baru dan perluasan bandara',
        'consulting_overall_02_role': 'Membandingkan waktu pembukaan, ukuran fasilitas, dan pembagian fungsi antara terminal baru dan '
                                      'terminal lama.',
        'consulting_overall_03_title': 'Perubahan tata letak sisi udara',
        'consulting_overall_03_role': 'Menilai dampak perubahan taxiway dan posisi parkir terhadap pergerakan pesawat serta arus kendaraan '
                                      'pelayanan darat.',
        'consulting_overall_04_title': 'Renovasi saat tetap beroperasi',
        'consulting_overall_04_role': 'Menilai fasilitas yang dapat ditutup bersamaan serta membandingkan rute sementara dan urutan '
                                      'konstruksi.',
        'consulting_overall_05_title': 'Proposal bersama desain dan rekayasa',
        'consulting_overall_05_role': 'Bergabung dalam proposal sebagai mitra teknis untuk simulasi dan penilaian kapasitas, lalu '
                                      'menjalankan analisis yang disepakati setelah kontrak diperoleh.',
        'consulting_overall_06_title': 'Strategi pengembangan bandara',
        'consulting_overall_06_role': 'Menilai permintaan, kapasitas, dan alternatif untuk mendukung penentuan waktu investasi serta '
                                      'ukuran fasilitas.',
        'consulting_tab_demand': 'Permintaan & Jadwal',
        'consulting_demand_intro': 'Menerjemahkan permintaan masa depan menjadi skenario operasi, kebutuhan fasilitas, dan keputusan '
                                   'perluasan.',
        'consulting_task_01_title': 'Permintaan lalu lintas dan penumpang masa depan',
        'consulting_task_01_description': 'Menyusun skenario tahun sasaran dan tahap pertumbuhan dari prakiraan serta data operasi yang '
                                          'ada untuk menilai kebutuhan fasilitas dan operasi.',
        'consulting_task_02_title': 'Permintaan hari desain dan jam puncak',
        'consulting_task_02_description': 'Menerjemahkan permintaan tahunan menjadi profil hari representatif, hari puncak, dan per jam '
                                          'untuk menetapkan beban yang harus ditampung fasilitas.',
        'consulting_task_03_title': 'Penyusunan jadwal penerbangan masa depan',
        'consulting_task_03_description': 'Menyusun jadwal hari desain berdasarkan permintaan, komposisi armada, pola maskapai, dan jam '
                                          'operasi, lalu menilai kelayakan operasionalnya.',
        'consulting_task_04_title': 'Komposisi armada dan pola maskapai',
        'consulting_task_04_description': 'Membandingkan pengaruh ukuran pesawat, komposisi maskapai dan rute, serta kelompok waktu '
                                          'kedatangan dan keberangkatan terhadap kebutuhan gerbang, posisi parkir, dan terminal.',
        'consulting_task_05_title': 'Segmen penumpang dan profil kedatangan',
        'consulting_task_05_description': 'Memodelkan waktu dan lokasi penumpang berangkat, tiba, dan transfer mencapai fasilitas, dengan '
                                          'memperhitungkan pola waktu kedatangan dan alokasi gerbang.',
        'consulting_task_06_title': 'Kesenjangan kapasitas dan pemicu perluasan',
        'consulting_task_06_description': 'Menguji pertumbuhan permintaan terhadap batas kapasitas dan ruang kapasitas tersisa untuk '
                                          'merekomendasikan ambang perluasan, perkiraan waktu, serta prioritas fasilitas.',
        'consulting_tab_terminal': 'Terminal & Sisi Darat',
        'consulting_terminal_intro': 'Menilai proses penumpang, tata letak fasilitas, relokasi maskapai, tahapan konstruksi, dan '
                                     'pengaturan akses.',
        'consulting_task_07_title': 'Ukuran dan kecukupan fasilitas terminal',
        'consulting_task_07_description': 'Menilai fasilitas pemrosesan dan area tunggu terhadap permintaan serta kriteria layanan untuk '
                                          'menentukan jumlah fasilitas dan jam operasi yang diperlukan.',
        'consulting_task_08_title': 'Proses keberangkatan dan rencana operasi',
        'consulting_task_08_description': 'Membandingkan pembukaan fasilitas, jam operasi, dan penempatan petugas untuk check-in, '
                                          'penyerahan bagasi mandiri, pemeriksaan boarding pass, keamanan, dan imigrasi keberangkatan.',
        'consulting_task_09_title': 'Kedatangan, pengambilan bagasi, dan bea cukai',
        'consulting_task_09_description': 'Memodelkan imigrasi kedatangan, pengambilan bagasi, dan bea cukai secara terpadu untuk menilai '
                                          'dampak perubahan satu tahap terhadap total waktu proses dan kepadatan pada tahap berikutnya.',
        'consulting_task_10_title': 'Arus transfer dan koneksi terminal',
        'consulting_task_10_description': 'Menilai keamanan transfer, pergerakan antargerbang, koridor, dan peron angkutan antarterminal '
                                          'dari sisi kepadatan serta waktu koneksi.',
        'consulting_task_11_title': 'Relokasi maskapai dan dampak fasilitas',
        'consulting_task_11_description': 'Membandingkan perpindahan maskapai antarterminal, concourse, zona check-in, atau gerbang '
                                          'terhadap distribusi penumpang, beban fasilitas, rute transfer, dan kepadatan ruang tunggu '
                                          'gerbang.',
        'consulting_task_12_title': 'Terminal baru dan perluasan bertahap',
        'consulting_task_12_description': 'Membandingkan ukuran, tata letak, peran, dan koneksi fasilitas dengan terminal lama untuk '
                                          'menilai kapasitas saat pembukaan dan tahap perluasan berikutnya.',
        'consulting_task_13_title': 'Renovasi saat bandara tetap beroperasi',
        'consulting_task_13_description': 'Menilai penutupan dan berkurangnya ketersediaan fasilitas untuk menentukan kombinasi penutupan '
                                          'yang layak serta pengaturan operasi sementara.',
        'consulting_task_14_title': 'Sirkulasi penumpang dan tata letak antrean',
        'consulting_task_14_description': 'Membandingkan lebar koridor, partisi, pengalihan rute, dan tata letak antrean terhadap jarak '
                                          'berjalan, kepadatan, serta waktu tinggal; kemudian merekomendasikan perbaikan ruang.',
        'consulting_task_15_title': 'Akses sisi darat dan simpul transportasi',
        'consulting_task_15_description': 'Menilai kedatangan penumpang dan kendaraan serta pilihan tata letak area antar-jemput terminal, '
                                          'parkir, jalan akses, dan simpul angkutan umum dalam lingkup yang disepakati.',
        'consulting_task_16_title': 'Kondisi gabungan dan skenario tekanan',
        'consulting_task_16_description': 'Menggabungkan permintaan puncak, keterlambatan penerbangan, penutupan, dan relokasi maskapai '
                                          'untuk menemukan area rentan serta membandingkan pilihan pengurangan kepadatan dan pemulihan.',
        'consulting_tab_airside': 'Sisi Udara',
        'consulting_airside_intro': 'Mengevaluasi rencana runway, taxiway, posisi parkir, dan fasilitas pendukung bersama operasi pesawat '
                                    'serta pelayanan darat.',
        'consulting_task_17_title': 'Kapasitas runway dan keterlambatan penerbangan',
        'consulting_task_17_description': 'Memodelkan mode operasi, waktu okupansi, separasi, dan lalu lintas terkonsentrasi untuk menilai '
                                          'kapasitas runway serta keterlambatan kedatangan dan keberangkatan, termasuk dalam jarak pandang '
                                          'rendah.',
        'consulting_task_18_title': 'Lokasi dan tata letak rapid-exit taxiway',
        'consulting_task_18_description': 'Membandingkan posisi dan jarak antar-rapid-exit taxiway berdasarkan karakteristik pendaratan '
                                          'pesawat dan pertimbangan okupansi runway.',
        'consulting_task_19_title': 'Perubahan tata letak sisi udara dan dampaknya',
        'consulting_task_19_description': 'Menilai dampak runway, taxiway, dan apron yang baru, diperpanjang, disambungkan ulang, atau '
                                          'ditutup terhadap rute, waktu taxi, titik hambatan, dan gangguan operasi.',
        'consulting_task_20_title': 'Alokasi posisi parkir dan pushback bersamaan',
        'consulting_task_20_description': 'Menilai kompatibilitas pesawat, alokasi posisi parkir kontak dan remote, okupansi, serta '
                                          'pergerakan bersamaan untuk merekomendasikan alternatif tata letak dan operasi.',
        'consulting_task_21_title': 'Pergerakan pesawat dan kendaraan pelayanan darat',
        'consulting_task_21_description': 'Memodelkan pergerakan dan pushback pesawat bersama tugas serta rute kendaraan untuk menilai '
                                          'kepadatan jalan layanan, gangguan di persilangan, dan rencana operasi kendaraan.',
        'consulting_task_22_title': 'Apron kargo dan operasi pesawat kargo',
        'consulting_task_22_description': 'Menilai kompatibilitas posisi parkir pesawat kargo besar, okupansi, rute akses, serta koneksi '
                                          'dengan terminal kargo dan logistik darat.',
        'consulting_task_23_title': 'Akses MRO, hanggar, dan GA/FBO',
        'consulting_task_23_description': 'Meninjau kompatibilitas pesawat, akses hanggar, rute penarikan, serta interaksi dengan apron '
                                          'dan jalan layanan di sekitarnya.',
        'consulting_task_24_title': 'Tata letak dan operasi fasilitas de-icing',
        'consulting_task_24_description': 'Menilai daya tampung bersamaan, rute masuk dan keluar, serta jarak bebas pesawat; kemudian '
                                          'membandingkan antrean dan keterlambatan keberangkatan pada waktu proses yang bervariasi.',
        'consulting_task_25_title': 'Penempatan ARFF, bahan bakar, dan fasilitas pendukung',
        'consulting_task_25_description': 'Menilai lokasi fasilitas penyelamatan dan pemadam kebakaran, bahan bakar, serta utilitas, rute '
                                          'akses, dan cakupan layanan untuk mendukung keputusan tata letak dan operasi.',
        'consulting_task_26_title': 'Visibilitas menara dan batasan halangan',
        'consulting_task_26_description': 'Membandingkan garis pandang dan titik buta, serta meninjau tumpang tindih obstacle limitation '
                                          'surfaces terkait rencana runway dan fasilitas sekitar pada tahap perencanaan.',
        'consulting_tab_digital': 'Kembaran Digital',
        'consulting_digital_intro': 'Memodelkan tahap pengembangan bandara, memvalidasi aturan operasi, dan membangun kemampuan analisis '
                                    'yang diperlukan proyek.',
        'consulting_task_27_title': 'Model bandara saat ini dan masa depan',
        'consulting_task_27_description': 'Menyiapkan masukan spasial dan memodelkan tata letak eksisting, pembukaan, perluasan antara, '
                                          'dan pengembangan akhir beserta fasilitas yang direncanakan pada setiap tahap.',
        'consulting_task_28_title': 'Model khusus bandara dan validasi operasional',
        'consulting_task_28_description': 'Mengonfigurasi tata letak khusus, aturan penggunaan fasilitas, dan prosedur operasi, lalu '
                                          'memvalidasi serta mengalibrasi terhadap pengamatan dan catatan operasi yang tersedia.',
        'consulting_task_29_title': 'Overlay desain dan visualisasi spasial',
        'consulting_task_29_description': 'Membandingkan rencana eksisting, alternatif, dan tahapan konstruksi, serta menjelaskan arus '
                                          'pesawat, kendaraan, dan penumpang melalui denah, model spasial, dan video simulasi.',
        'consulting_task_30_title': 'KPI dan fitur analisis khusus',
        'consulting_task_30_description': 'Menentukan ukuran kinerja khusus bandara, termasuk operasi gerbang bersamaan dan pelampauan '
                                          'waktu transfer, serta mengonfigurasi masukan, keluaran, dan fungsi akses hasil yang diperlukan.',
        'consulting_scope_note': 'Lingkup, detail model, dan kriteria penilaian disepakati berdasarkan data bandara, kondisi operasi, '
                                 'serta kebutuhan proyek Anda. Studi tambahan, pengembangan fitur, dan integrasi sistem eksternal '
                                 'ditetapkan lingkupnya beserta jadwal yang diperlukan.',
        'consulting_expertise_heading': 'Teknologi dan pengalaman bandara',
        'consulting_expertise_origin': 'Team Flexa berawal dari program usaha internal Incheon International Airport Corporation. Tim kami '
                                       'telah menangani peningkatan operasi dan perluasan Bandara Incheon, serta penugasan dalam bisnis '
                                       'bandara luar negeri perusahaan tersebut.',
        'consulting_expertise_01_title': 'Perangkat lunak milik sendiri',
        'consulting_expertise_01_description': 'Kami mengembangkan dan memiliki perangkat lunak sendiri, menyesuaikan model serta fungsi '
                                               'dengan studi sambil mengurangi kebutuhan alat analisis terpisah atau staf khusus.',
        'consulting_expertise_02_title': 'KPI dan fitur analisis khusus',
        'consulting_expertise_02_description': 'Kami menggunakan ukuran kinerja, kriteria penilaian, dan format laporan Anda; pengembangan '
                                               'atau integrasi tambahan disepakati jika fungsi yang ada belum memadai.',
        'consulting_expertise_03_title': 'Aturan dan tata letak khusus bandara',
        'consulting_expertise_03_description': 'Kami memodelkan koneksi terminal, aturan penggunaan fasilitas maskapai, konfigurasi posisi '
                                               'parkir, rute pelayanan darat, dan pembatasan berdasarkan waktu.',
        'consulting_expertise_04_title': 'Data dan model yang ada',
        'consulting_expertise_04_description': 'Kami menggunakan data bandara, penerbangan, fasilitas, serta model yang tersedia untuk '
                                               'mengurangi waktu persiapan, dengan validasi terhadap pengamatan Anda dan kriteria yang '
                                               'disepakati.',
        'consulting_expertise_05_title': 'Arus pesawat, kendaraan, dan penumpang yang terhubung',
        'consulting_expertise_05_description': 'Pergerakan pesawat dan tugas kendaraan dimodelkan bersama; alokasi gerbang dan kedatangan '
                                               'penumpang menghubungkan studi sisi udara dengan terminal untuk menilai dampak perubahan '
                                               'fasilitas secara lebih luas.',
        'consulting_engagements_heading': 'Bekerja bersama kami',
        'consulting_engagements_terms': 'Kerja sama dapat berupa konsultasi saja atau konsultasi dengan fitur maupun lisensi perangkat '
                                        'lunak tertentu. Akses langsung ke hasil atau fungsi tinjauan lanjutan beserta ketentuan '
                                        'penggunaannya disepakati terpisah.',
        'consulting_engagements_01_title': 'Konsultasi berbasis proyek',
        'consulting_engagements_01_application': 'Perluasan bandara, relokasi maskapai, rencana konstruksi, dan kebutuhan perencanaan lain '
                                                 'yang telah ditetapkan.',
        'consulting_engagements_01_role': 'Kami mengembangkan model, membandingkan opsi, dan merekomendasikan perbaikan, dengan temuan '
                                          'yang disiapkan untuk tinjauan perencanaan serta anggaran.',
        'consulting_engagements_02_title': 'Proposal bersama dan pelaksanaan proyek',
        'consulting_engagements_02_application': 'Simulasi dan penilaian kapasitas dalam penugasan desain, rekayasa, dan konsultasi.',
        'consulting_engagements_02_role': 'Pada tahap proposal, kami menyepakati metode, tanggung jawab, jadwal, dan biaya; setelah '
                                          'kontrak diperoleh, kami melakukan analisis yang disepakati untuk menguji desain serta '
                                          'membandingkan alternatif.',
        'consulting_engagements_03_title': 'Kemitraan teknis berkelanjutan',
        'consulting_engagements_03_application': 'Analisis spesialis untuk beberapa proyek bandara.',
        'consulting_engagements_03_role': 'Kami menyediakan tinjauan desain, analisis skenario, dan saran teknis selama periode yang '
                                          'disepakati, tanpa memerlukan tim analisis internal khusus.',
        'consulting_deliverables_heading': 'Hasil pekerjaan',
        'consulting_deliverables_usage_rights': 'Hak dan masa penggunaan data, model, akun, atau fungsi solusi yang disediakan ditetapkan '
                                                'sesuai kerja sama.',
        'consulting_deliverables_01_title': 'Laporan konsultasi',
        'consulting_deliverables_01_use': 'Laporan teknis atau ringkasan eksekutif yang mencakup tujuan, penilaian opsi, rekomendasi, dan '
                                          'prioritas investasi.',
        'consulting_deliverables_02_title': 'Laporan web HTML',
        'consulting_deliverables_02_use': 'Tinjauan skenario, perbandingan, dan visualisasi spasial melalui browser.',
        'consulting_deliverables_03_title': 'PDF dan DOCX',
        'consulting_deliverables_03_use': 'Penyerahan dokumen proyek, tinjauan internal, penyuntingan bersama, dan distribusi cetak.',
        'consulting_deliverables_04_title': 'Video dan gambar hasil rendering',
        'consulting_deliverables_04_use': 'Video simulasi, perbandingan alternatif tata letak, dan rendering spasial untuk rapat serta '
                                          'komunikasi pemangku kepentingan.',
        'consulting_deliverables_05_title': 'Data, model, dan komponen solusi terpilih',
        'consulting_deliverables_05_use': 'Dataset, paket model, akun akses, atau fungsi yang disediakan sesuai kesepakatan kerja sama.',
        'consulting_programme_heading': 'Jadwal dan biaya',
        'consulting_programme_01_title': 'Jadwal berbasis proyek',
        'consulting_programme_01_description': 'Kami menyelaraskan rencana kerja dengan jadwal proyek Anda, dengan mempertimbangkan '
                                               'lingkup studi, penyiapan data, validasi model, dan tinjauan.',
        'consulting_programme_02_title': 'Dukungan periode tetap',
        'consulting_programme_02_description': 'Tinjauan desain, analisis skenario, dan saran teknis tersedia untuk periode yang '
                                               'disepakati, misalnya satu, tiga, atau enam bulan; beban kerja, frekuensi, dan waktu '
                                               'respons ditetapkan terpisah.',
        'consulting_programme_03_title': 'Pelaksanaan bertahap',
        'consulting_programme_03_description': 'Menugaskan studi pada tahap konsep, desain awal, desain rinci, dan konstruksi, dengan '
                                               'tinjauan tambahan ketika rencana berubah.',
        'consulting_programme_04_title': 'Penetapan biaya',
        'consulting_programme_04_description': 'Biaya mempertimbangkan lingkup, skala proyek, durasi, jumlah alternatif, dan kebutuhan '
                                               'pengembangan khusus.',
        'footer_copyright': 'Hak cipta 2026 TeamFlexa CO., LTD. Seluruh hak dilindungi.',
        'flexa_about_title': 'Tentang Flexa',
        'flexa_about_p1': 'Flexa adalah merek yang ditawarkan oleh TeamFlexa CO., LTD., perusahaan spesialis solusi bandara yang mengurai '
                          'kompleksitas operasi bandara melalui data, serta menghadirkan hasil optimal dengan teknologi simulasi dan '
                          'analitik berbasis AI. Kami melampaui analisis dengan memberikan wawasan yang dapat ditindaklanjuti untuk '
                          'mewujudkan perbaikan operasional yang nyata.',
        'flexa_about_p2': 'Berawal sebagai usaha rintisan internal di Bandara Internasional Incheon, TeamFlexa memanfaatkan pengalaman dan '
                          'data dari salah satu lingkungan bandara terkemuka di dunia. Melalui merek Flexa, kami menyediakan konsultasi '
                          'dan solusi menyeluruh, dari optimalisasi operasi terminal hingga strategi infrastruktur jangka menengah dan '
                          'panjang, agar klien dapat merumuskan tantangan kompleks secara kuantitatif dan mengambil keputusan yang paling '
                          'efektif.',
        'flexa_about_p3': 'Melayani bandara, operator bandara, serta perusahaan rekayasa dan konstruksi di seluruh dunia, TeamFlexa '
                          'mendiagnosis masalah dengan cepat dan tepat, merancang strategi sesuai kebutuhan, dan memastikan '
                          'pelaksanaannya. Kami mendefinisikan ulang standar operasi bandara dan menjadi mitra terdepan dalam pengambilan '
                          'keputusan berbasis data di pasar global.'},
 'ru': {'consulting_eyebrow': 'Консалтинговые услуги',
        'consulting_heading': 'Аэропортовый консалтинг',
        'consulting_intro': 'Планирование, моделирование и техническая поддержка для аэропортов и инженерных команд.',
        'consulting_projects_heading': 'Применение в проектах',
        'consulting_tab_overall': 'Обзор',
        'consulting_tabs_aria': 'Направления консалтинга',
        'consulting_overall_intro': 'Типовые проекты включают новые аэропорты и терминалы, расширение, реконструкцию без остановки работы, '
                                    'перевод авиакомпаний или перенос объектов, поэтапные инвестиции и совершенствование операций.',
        'consulting_overall_01_title': 'Перевод авиакомпаний',
        'consulting_overall_01_role': 'Оценить, смогут ли зоны регистрации, досмотра и обслуживания трансферных пассажиров принять '
                                      'переводимые авиакомпании, и сравнить подходящие планировочные решения.',
        'consulting_overall_02_title': 'Новые терминалы и расширение аэропорта',
        'consulting_overall_02_role': 'Сравнить сроки открытия, размеры объектов и распределение функций между новыми и существующими '
                                      'терминалами.',
        'consulting_overall_03_title': 'Изменение планировки аэродрома',
        'consulting_overall_03_role': 'Оценить, как изменения рулёжных дорожек и мест стоянки влияют на движение воздушных судов и потоки '
                                      'транспорта наземного обслуживания.',
        'consulting_overall_04_title': 'Реконструкция без остановки работы',
        'consulting_overall_04_role': 'Оценить, какие объекты можно закрыть одновременно, и сравнить временные маршруты и '
                                      'последовательность строительных работ.',
        'consulting_overall_05_title': 'Совместные проектные и инженерные предложения',
        'consulting_overall_05_role': 'Участвовать в подготовке предложений в качестве технического партнёра по моделированию и оценке '
                                      'пропускной способности, а после получения контракта выполнить согласованный анализ.',
        'consulting_overall_06_title': 'Стратегия развития аэропорта',
        'consulting_overall_06_role': 'Оценить спрос, пропускную способность и альтернативы, чтобы обосновать сроки инвестиций и размеры '
                                      'объектов.',
        'consulting_tab_demand': 'Спрос и расписания',
        'consulting_demand_intro': 'Преобразовать прогноз спроса в эксплуатационные сценарии, требования к объектам и решения по '
                                   'расширению.',
        'consulting_task_01_title': 'Будущий объём перевозок и пассажирский спрос',
        'consulting_task_01_description': 'Разработать сценарии для расчётного года и этапов роста на основе имеющихся прогнозов и '
                                          'эксплуатационных данных для оценки требований к объектам и операциям.',
        'consulting_task_02_title': 'Нагрузка расчётного дня и пикового часа',
        'consulting_task_02_description': 'Преобразовать годовой спрос в профили типового дня, пикового дня и почасовой нагрузки, чтобы '
                                          'определить объёмы, которые должны обслуживать объекты.',
        'consulting_task_03_title': 'Формирование перспективного расписания полётов',
        'consulting_task_03_description': 'Разработать расписания расчётного дня с учётом спроса, состава парка, особенностей работы '
                                          'авиакомпаний и часов работы, затем оценить их эксплуатационную реализуемость.',
        'consulting_task_04_title': 'Состав парка и особенности работы авиакомпаний',
        'consulting_task_04_description': 'Сравнить, как размеры воздушных судов, состав авиакомпаний и маршрутов, а также волны прилётов '
                                          'и вылетов влияют на потребность в выходах на посадку, местах стоянки и терминальной '
                                          'инфраструктуре.',
        'consulting_task_05_title': 'Категории пассажиров и профили прибытия',
        'consulting_task_05_description': 'Смоделировать, когда и куда прибывают вылетающие, прилетающие и трансферные пассажиры, с учётом '
                                          'времени их появления в аэропорту и распределения выходов на посадку.',
        'consulting_task_06_title': 'Дефицит пропускной способности и условия расширения',
        'consulting_task_06_description': 'Сопоставить рост спроса с предельной пропускной способностью и её резервом, чтобы рекомендовать '
                                          'пороговые значения для расширения, ориентировочные сроки и приоритетные объекты.',
        'consulting_tab_terminal': 'Терминал и привокзальная зона',
        'consulting_terminal_intro': 'Оценить процессы обслуживания пассажиров, планировку объектов, перевод авиакомпаний, этапность '
                                     'строительства и организацию доступа.',
        'consulting_task_07_title': 'Размеры и достаточность объектов терминала',
        'consulting_task_07_description': 'Оценить зоны обслуживания и ожидания с учётом спроса и критериев качества обслуживания, чтобы '
                                          'определить необходимое количество объектов и часы их работы.',
        'consulting_task_08_title': 'Процессы вылета и эксплуатационные планы',
        'consulting_task_08_description': 'Сравнить порядок открытия объектов, часы работы и численность персонала для регистрации, '
                                          'самостоятельной сдачи багажа, проверки посадочных талонов, досмотра и пограничного контроля на '
                                          'вылете.',
        'consulting_task_09_title': 'Прилёт, выдача багажа и таможня',
        'consulting_task_09_description': 'Совместно смоделировать пограничный контроль на прилёте, выдачу багажа и таможенный контроль, '
                                          'чтобы оценить влияние изменений на одном этапе на общее время обслуживания и перегрузку '
                                          'последующих этапов.',
        'consulting_task_10_title': 'Трансферные потоки и связи между терминалами',
        'consulting_task_10_description': 'Оценить перегрузку и время пересадки в зонах трансферного досмотра, на маршрутах между выходами '
                                          'на посадку, в коридорах и на платформах межтерминального транспорта.',
        'consulting_task_11_title': 'Перевод авиакомпаний и влияние на объекты',
        'consulting_task_11_description': 'Сравнить перевод авиакомпаний между терминалами, галереями, зонами регистрации или выходами на '
                                          'посадку по распределению пассажиров, нагрузке на объекты, трансферным маршрутам и перегрузке '
                                          'залов ожидания у выходов.',
        'consulting_task_12_title': 'Новые терминалы и поэтапное расширение',
        'consulting_task_12_description': 'Сравнить размеры, планировку, функции и связи с существующими терминалами, чтобы оценить '
                                          'пропускную способность при открытии и на последующих этапах расширения.',
        'consulting_task_13_title': 'Реконструкция действующего аэропорта',
        'consulting_task_13_description': 'Оценить закрытия и снижение доступности объектов, чтобы определить допустимые сочетания '
                                          'закрытий и временные схемы работы.',
        'consulting_task_14_title': 'Движение пассажиров и организация очередей',
        'consulting_task_14_description': 'Сравнить ширину коридоров, перегородки, обходные маршруты и схемы очередей по длине пути, '
                                          'перегрузке и времени пребывания, затем рекомендовать планировочные улучшения.',
        'consulting_task_15_title': 'Подъезды и наземные транспортные связи',
        'consulting_task_15_description': 'В рамках согласованного объёма работ оценить прибытие пассажиров и транспорта, а также варианты '
                                          'планировки зон посадки и высадки у терминала, парковок, подъездных дорог и узлов общественного '
                                          'транспорта.',
        'consulting_task_16_title': 'Сочетание факторов и стресс-сценарии',
        'consulting_task_16_description': 'Совместить пиковый спрос, задержки рейсов, закрытия объектов и перевод авиакомпаний, чтобы '
                                          'выявить уязвимые зоны и сравнить меры по снижению перегрузки и восстановлению работы.',
        'consulting_tab_airside': 'Аэродром',
        'consulting_airside_intro': 'Оценить планы взлётно-посадочных полос, рулёжных дорожек, мест стоянки и вспомогательных объектов с '
                                    'учётом движения воздушных судов и наземного обслуживания.',
        'consulting_task_17_title': 'Пропускная способность ВПП и задержки рейсов',
        'consulting_task_17_description': 'Смоделировать режимы работы, занятость ВПП, интервалы эшелонирования и концентрацию движения, '
                                          'чтобы оценить пропускную способность полосы и задержки прилётов и вылетов, в том числе при '
                                          'низкой видимости.',
        'consulting_task_18_title': 'Размещение и планировка скоростных рулёжных дорожек',
        'consulting_task_18_description': 'Сравнить расположение и интервалы между скоростными рулёжными дорожками с учётом посадочных '
                                          'характеристик воздушных судов и времени занятости ВПП.',
        'consulting_task_19_title': 'Изменения планировки аэродрома и их последствия',
        'consulting_task_19_description': 'Оценить, как новые, удлинённые, переподключённые или закрытые ВПП, рулёжные дорожки и перроны '
                                          'влияют на маршруты, время руления, узкие места и взаимные помехи при выполнении операций.',
        'consulting_task_20_title': 'Распределение мест стоянки и одновременная буксировка',
        'consulting_task_20_description': 'Оценить совместимость с типами воздушных судов, распределение контактных и удалённых стоянок, '
                                          'их занятость и одновременные перемещения, чтобы рекомендовать варианты планировки и '
                                          'эксплуатации.',
        'consulting_task_21_title': 'Движение воздушных судов и транспорта наземного обслуживания',
        'consulting_task_21_description': 'Смоделировать движение и буксировку воздушных судов совместно с задачами и маршрутами '
                                          'транспорта, чтобы оценить перегрузку служебных дорог, помехи на пересечениях и планы работы '
                                          'транспорта.',
        'consulting_task_22_title': 'Грузовые перроны и эксплуатация грузовых воздушных судов',
        'consulting_task_22_description': 'Оценить пригодность стоянок для крупных грузовых воздушных судов, их занятость, маршруты '
                                          'доступа и связи с грузовыми терминалами и наземной логистикой.',
        'consulting_task_23_title': 'Доступ к MRO, ангарам и GA/FBO',
        'consulting_task_23_description': 'Проверить совместимость с типами воздушных судов, доступ к ангарам, маршруты буксировки и '
                                          'взаимодействие с прилегающими перронами и служебными дорогами.',
        'consulting_task_24_title': 'Планировка и работа площадок противообледенительной обработки',
        'consulting_task_24_description': 'Оценить одновременное размещение воздушных судов, маршруты въезда и выезда и безопасные '
                                          'расстояния, затем сравнить очереди и задержки вылета при различной продолжительности обработки.',
        'consulting_task_25_title': 'Размещение ARFF, топливных и вспомогательных объектов',
        'consulting_task_25_description': 'Оценить расположение аварийно-спасательных и противопожарных, топливных и инженерных объектов, '
                                          'пути доступа и зоны обслуживания для обоснования планировочных и эксплуатационных решений.',
        'consulting_task_26_title': 'Обзор с диспетчерской вышки и ограничения по препятствиям',
        'consulting_task_26_description': 'Сравнить линии обзора и слепые зоны, а на стадии планирования проверить пересечения с '
                                          'поверхностями ограничения препятствий, связанные с планами ВПП и окружающих объектов.',
        'consulting_tab_digital': 'Цифровые двойники',
        'consulting_digital_intro': 'Смоделировать этапы развития аэропорта, проверить эксплуатационные правила и создать необходимые для '
                                    'проекта средства анализа.',
        'consulting_task_27_title': 'Модели текущего и будущего состояния аэропорта',
        'consulting_task_27_description': 'Подготовить пространственные исходные данные и смоделировать существующую планировку, '
                                          'конфигурацию к открытию, промежуточные этапы расширения и конечное развитие с объектами, '
                                          'предусмотренными для каждого этапа.',
        'consulting_task_28_title': 'Модели с учётом особенностей аэропорта и эксплуатационная проверка',
        'consulting_task_28_description': 'Настроить индивидуальные планировки, правила использования объектов и эксплуатационные '
                                          'процедуры, затем проверить и откалибровать модели по доступным наблюдениям и эксплуатационным '
                                          'записям.',
        'consulting_task_29_title': 'Наложение проектных решений и пространственная визуализация',
        'consulting_task_29_description': 'Сравнить существующие планы, альтернативы и этапы строительства, а также показать потоки '
                                          'воздушных судов, транспорта и пассажиров с помощью планов, пространственных моделей и '
                                          'видеозаписей моделирования.',
        'consulting_task_30_title': 'Индивидуальные KPI и функции анализа',
        'consulting_task_30_description': 'Определить показатели для конкретного аэропорта, включая одновременные операции у выходов на '
                                          'посадку и превышения времени пересадки, и настроить необходимые входные данные, выходные '
                                          'результаты и функции доступа к ним.',
        'consulting_scope_note': 'Объём работ, детализация модели и критерии оценки согласуются с учётом данных аэропорта, условий '
                                 'эксплуатации и требований проекта. Дополнительные исследования, разработка функций и интеграция с '
                                 'внешними системами определяются вместе с необходимыми сроками.',
        'consulting_expertise_heading': 'Технологии и опыт работы с аэропортами',
        'consulting_expertise_origin': 'Team Flexa выросла из программы внутреннего предпринимательства Incheon International Airport '
                                       'Corporation. Наша команда работала над совершенствованием операций и расширением аэропорта Инчхон, '
                                       'а также участвовала в зарубежных аэропортовых проектах корпорации.',
        'consulting_expertise_01_title': 'Собственное программное обеспечение',
        'consulting_expertise_01_description': 'Мы разрабатываем собственное программное обеспечение и владеем им, адаптируя модели и '
                                               'функции к исследованию и снижая потребность в отдельных аналитических инструментах или '
                                               'специалистах.',
        'consulting_expertise_02_title': 'Индивидуальные KPI и функции анализа',
        'consulting_expertise_02_description': 'Мы используем ваши показатели эффективности, критерии оценки и форматы отчётности, '
                                               'согласуя дополнительную разработку или интеграцию, если имеющихся функций недостаточно.',
        'consulting_expertise_03_title': 'Правила и планировки конкретного аэропорта',
        'consulting_expertise_03_description': 'Мы моделируем связи между терминалами, правила использования объектов авиакомпаниями, '
                                               'конфигурации стоянок, маршруты наземного обслуживания и ограничения по времени.',
        'consulting_expertise_04_title': 'Имеющиеся данные и модели',
        'consulting_expertise_04_description': 'Мы используем доступные данные об аэропортах, рейсах и объектах, а также существующие '
                                               'модели, чтобы сократить время подготовки, и проверяем их по вашим наблюдениям и '
                                               'согласованным критериям.',
        'consulting_expertise_05_title': 'Связанные потоки воздушных судов, транспорта и пассажиров',
        'consulting_expertise_05_description': 'Движение воздушных судов и задачи транспорта моделируются совместно; распределение выходов '
                                               'на посадку и прибытие пассажиров связывают исследования аэродрома и терминала, позволяя '
                                               'оценивать более широкие последствия изменений объектов.',
        'consulting_engagements_heading': 'Сотрудничество с нами',
        'consulting_engagements_terms': 'Сотрудничество возможно в формате консалтинга либо консалтинга с предоставлением выбранных '
                                        'функций или лицензий ПО. Прямой доступ к результатам или функциям последующего анализа и условия '
                                        'их использования согласуются отдельно.',
        'consulting_engagements_01_title': 'Консалтинг по отдельным проектам',
        'consulting_engagements_01_application': 'Расширение аэропорта, перевод авиакомпаний, планы строительства и другие конкретные '
                                                 'задачи планирования.',
        'consulting_engagements_01_role': 'Мы разрабатываем модели, сравниваем варианты и рекомендуем улучшения, подготавливая результаты '
                                          'для рассмотрения планов и бюджетов.',
        'consulting_engagements_02_title': 'Совместные предложения и выполнение проектов',
        'consulting_engagements_02_application': 'Моделирование и оценка пропускной способности в составе проектных, инженерных и '
                                                 'консалтинговых работ.',
        'consulting_engagements_02_role': 'На этапе предложения мы согласуем метод, обязанности, график и стоимость; после получения '
                                          'контракта выполняем согласованный анализ для проверки проектных решений и сравнения '
                                          'альтернатив.',
        'consulting_engagements_03_title': 'Постоянное техническое партнёрство',
        'consulting_engagements_03_application': 'Специализированный анализ для нескольких аэропортовых проектов.',
        'consulting_engagements_03_role': 'Мы предоставляем проверку проектных решений, сценарный анализ и технические консультации в '
                                          'течение согласованного периода, без необходимости создавать собственную специализированную '
                                          'аналитическую команду.',
        'consulting_deliverables_heading': 'Результаты работ',
        'consulting_deliverables_usage_rights': 'Права и сроки использования предоставляемых данных, моделей, учётных записей или функций '
                                                'решения определяются для конкретного договора.',
        'consulting_deliverables_01_title': 'Консалтинговые отчёты',
        'consulting_deliverables_01_use': 'Технические отчёты или резюме для руководства с целями, оценкой вариантов, рекомендациями и '
                                          'инвестиционными приоритетами.',
        'consulting_deliverables_02_title': 'Веб-отчёты в HTML',
        'consulting_deliverables_02_use': 'Просмотр сценариев, сравнений и пространственных визуализаций в браузере.',
        'consulting_deliverables_03_title': 'PDF и DOCX',
        'consulting_deliverables_03_use': 'Представление проектных материалов, внутреннее согласование, совместное редактирование и '
                                          'распространение в печатном виде.',
        'consulting_deliverables_04_title': 'Видео и визуализации',
        'consulting_deliverables_04_use': 'Видеозаписи моделирования, сравнения вариантов планировки и пространственные визуализации для '
                                          'совещаний и взаимодействия с заинтересованными сторонами.',
        'consulting_deliverables_05_title': 'Данные, модели и выбранные компоненты решения',
        'consulting_deliverables_05_use': 'Согласованные наборы данных, пакеты моделей, учётные записи или функции, предоставляемые в '
                                          'рамках договора.',
        'consulting_programme_heading': 'Сроки и стоимость',
        'consulting_programme_01_title': 'График под задачи проекта',
        'consulting_programme_01_description': 'Мы согласуем график с вашим проектом, учитывая объём исследования, подготовку данных, '
                                               'проверку модели и этапы рассмотрения результатов.',
        'consulting_programme_02_title': 'Поддержка на определённый срок',
        'consulting_programme_02_description': 'Проверка проектных решений, сценарный анализ и технические консультации доступны на '
                                               'согласованные периоды, например один, три или шесть месяцев; объём работ, периодичность и '
                                               'сроки ответа согласуются отдельно.',
        'consulting_programme_03_title': 'Поэтапное выполнение',
        'consulting_programme_03_description': 'Заказывайте исследования на стадиях концепции, предварительного и детального '
                                               'проектирования и строительства, с дополнительными проверками по мере изменения планов.',
        'consulting_programme_04_title': 'Стоимость',
        'consulting_programme_04_description': 'Стоимость зависит от объёма работ, масштаба проекта, продолжительности, числа альтернатив '
                                               'и требований к индивидуальной разработке.',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. Все права защищены.',
        'flexa_about_title': 'О Flexa',
        'flexa_about_p1': 'Flexa — бренд компании TeamFlexa CO., LTD., специализирующейся на решениях для аэропортов. Компания раскрывает '
                          'сложные взаимосвязи аэропортовых операций с помощью данных и добивается оптимальных результатов благодаря '
                          'технологиям моделирования и аналитике на основе ИИ. Мы не ограничиваемся анализом: наши практические выводы '
                          'помогают добиваться реальных улучшений в работе аэропорта.',
        'flexa_about_p2': 'TeamFlexa зародилась как внутренний венчурный проект в Международном аэропорту Инчхон и опирается на опыт и '
                          'данные одного из ведущих аэропортов мира. Под брендом Flexa мы предоставляем комплексный консалтинг и решения — '
                          'от оптимизации работы терминалов до средне- и долгосрочной стратегии развития инфраструктуры. Это позволяет '
                          'клиентам количественно определять сложные задачи и принимать наиболее эффективные решения.',
        'flexa_about_p3': 'Работая с аэропортами, аэропортовыми операторами, инженерными и строительными компаниями по всему миру, '
                          'TeamFlexa быстро и точно выявляет проблемы, разрабатывает индивидуальные стратегии и обеспечивает их '
                          'реализацию. Мы переосмысливаем стандарты работы аэропортов и выступаем ведущим партнёром в принятии решений на '
                          'основе данных на мировом рынке.'},
 'uz': {'consulting_eyebrow': 'Konsalting xizmatlari',
        'consulting_heading': 'Aeroport konsaltingi',
        'consulting_intro': 'Aeroportlar va muhandislik guruhlari uchun rejalashtirish, simulyatsiya va texnik yordam.',
        'consulting_projects_heading': 'Loyihalarda qo‘llanishi',
        'consulting_tab_overall': 'Umumiy',
        'consulting_tabs_aria': 'Konsalting yo‘nalishlari',
        'consulting_overall_intro': 'Odatdagi loyihalar yangi aeroport va terminallar, kengaytirish, faoliyatni to‘xtatmasdan '
                                    'rekonstruksiya qilish, aviakompaniya yoki obyektlarni ko‘chirish, bosqichma-bosqich investitsiya va '
                                    'operatsiyalarni yaxshilashni qamrab oladi.',
        'consulting_overall_01_title': 'Aviakompaniyalarni ko‘chirish',
        'consulting_overall_01_role': 'Ro‘yxatdan o‘tish, xavfsizlik nazorati va transfer obyektlari ko‘chiriladigan aviakompaniyalarni '
                                      'qabul qila olishini baholash hamda mos joylashuvlarni solishtirish.',
        'consulting_overall_02_title': 'Yangi terminallar va aeroportni kengaytirish',
        'consulting_overall_02_role': 'Ochilish muddatlari, obyektlar hajmi hamda yangi va mavjud terminallar o‘rtasidagi vazifalar '
                                      'taqsimotini solishtirish.',
        'consulting_overall_03_title': 'Aerodrom hududi rejasini o‘zgartirish',
        'consulting_overall_03_role': 'O‘zgartirilgan rullash yo‘laklari va turargohlarning havo kemalari hamda yerusti xizmat transporti '
                                      'harakatiga ta’sirini baholash.',
        'consulting_overall_04_title': 'Faoliyatni to‘xtatmasdan rekonstruksiya qilish',
        'consulting_overall_04_role': 'Qaysi obyektlarni bir vaqtda yopish mumkinligini baholash, vaqtinchalik yo‘nalishlar va qurilish '
                                      'ketma-ketligini solishtirish.',
        'consulting_overall_05_title': 'Qo‘shma loyihalash va muhandislik takliflari',
        'consulting_overall_05_role': 'Simulyatsiya va o‘tkazish qobiliyatini baholash bo‘yicha texnik hamkor sifatida takliflarda '
                                      'qatnashish, shartnoma olingach kelishilgan tahlilni bajarish.',
        'consulting_overall_06_title': 'Aeroportni rivojlantirish strategiyasi',
        'consulting_overall_06_role': 'Investitsiya muddati va obyektlar hajmini belgilash uchun talab, o‘tkazish qobiliyati va muqobil '
                                      'variantlarni baholash.',
        'consulting_tab_demand': 'Talab va jadvallar',
        'consulting_demand_intro': 'Kelajakdagi talabni operatsion ssenariylar, obyektlarga bo‘lgan ehtiyoj va kengaytirish qarorlariga '
                                   'aylantirish.',
        'consulting_task_01_title': 'Kelajakdagi parvoz va yo‘lovchi talabi',
        'consulting_task_01_description': 'Mavjud prognozlar va operatsion ma’lumotlar asosida maqsadli yil hamda o‘sish bosqichlari '
                                          'ssenariylarini tuzib, obyektlar va operatsiyalarga bo‘lgan talabni baholash.',
        'consulting_task_02_title': 'Hisobiy kun va eng tig‘iz soat talabi',
        'consulting_task_02_description': 'Obyektlar ko‘tara olishi kerak bo‘lgan yuklamani belgilash uchun yillik talabni namunaviy kun, '
                                          'eng tig‘iz kun va soatlik profillarga aylantirish.',
        'consulting_task_03_title': 'Kelajakdagi parvozlar jadvalini tuzish',
        'consulting_task_03_description': 'Talab, havo kemalari parki tarkibi, aviakompaniyalar faoliyat xususiyatlari va ish vaqtiga '
                                          'asoslangan hisobiy kun jadvallarini tuzish, so‘ng amaliy bajarilish imkoniyatini baholash.',
        'consulting_task_04_title': 'Havo kemalari parki va aviakompaniyalar tarkibi',
        'consulting_task_04_description': 'Havo kemalari o‘lchami, aviakompaniya va yo‘nalishlar tarkibi hamda kelish-ketish reyslari '
                                          'guruhlanishining chiqish darvozalari, turargohlar va terminal talabiga ta’sirini solishtirish.',
        'consulting_task_05_title': 'Yo‘lovchi guruhlari va kelish profillari',
        'consulting_task_05_description': 'Jo‘nayotgan, kelayotgan va transfer yo‘lovchilarining obyektlarga qachon va qayerdan yetib '
                                          'kelishini modellashtirish; bunda kelish vaqti xususiyatlari va chiqish darvozalari taqsimoti '
                                          'hisobga olinadi.',
        'consulting_task_06_title': 'Quvvat yetishmovchiligi va kengaytirish mezonlari',
        'consulting_task_06_description': 'Kengaytirish chegaralari, taxminiy muddatlar va ustuvor obyektlarni tavsiya qilish uchun '
                                          'ortayotgan talabni o‘tkazish qobiliyati chegaralari hamda mavjud zaxira bilan tekshirish.',
        'consulting_tab_terminal': 'Terminal va umumiy hudud',
        'consulting_terminal_intro': 'Yo‘lovchilarga xizmat ko‘rsatish, obyektlar joylashuvi, aviakompaniyalarni ko‘chirish, qurilish '
                                     'bosqichlari va kirib kelish tartibini baholash.',
        'consulting_task_07_title': 'Terminal obyektlari hajmi va yetarliligi',
        'consulting_task_07_description': 'Kerakli obyektlar soni va ish vaqtini aniqlash uchun xizmat punktlari hamda kutish joylarini '
                                          'talab va xizmat mezonlariga nisbatan baholash.',
        'consulting_task_08_title': 'Jo‘nash jarayonlari va operatsion rejalar',
        'consulting_task_08_description': 'Ro‘yxatdan o‘tish, bagajni mustaqil topshirish, chiqish talonini tekshirish, xavfsizlik va '
                                          'chiqish pasport nazorati punktlarida ochilish, ish vaqti hamda xodimlar taqsimotini '
                                          'solishtirish.',
        'consulting_task_09_title': 'Kelish, bagaj olish va bojxona',
        'consulting_task_09_description': 'Bir bosqichdagi o‘zgarishning umumiy xizmat vaqti va keyingi bosqichlardagi tirbandlikka '
                                          'ta’sirini baholash uchun kirish pasport nazorati, bagaj olish va bojxonani birgalikda '
                                          'modellashtirish.',
        'consulting_task_10_title': 'Transfer oqimlari va terminallar o‘rtasidagi bog‘lanish',
        'consulting_task_10_description': 'Transfer xavfsizlik nazorati, darvozalararo harakat, yo‘laklar va terminallararo transport '
                                          'platformalarini tirbandlik hamda ulanish vaqti bo‘yicha baholash.',
        'consulting_task_11_title': 'Aviakompaniyalarni ko‘chirish va obyektlarga ta’siri',
        'consulting_task_11_description': 'Aviakompaniyalarni terminallar, chiqish zallari, ro‘yxatdan o‘tish zonalari yoki darvozalar '
                                          'o‘rtasida ko‘chirishni yo‘lovchi taqsimoti, obyektlar yuklamasi, transfer yo‘llari va kutish '
                                          'zali tirbandligi bo‘yicha solishtirish.',
        'consulting_task_12_title': 'Yangi terminallar va bosqichli kengaytirish',
        'consulting_task_12_description': 'Ochilish va keyingi kengaytirish bosqichlaridagi o‘tkazish qobiliyatini baholash uchun '
                                          'obyektlar hajmi, joylashuvi, vazifalari va mavjud terminallar bilan bog‘lanishini solishtirish.',
        'consulting_task_13_title': 'Aeroport ishlayotgan paytda rekonstruksiya',
        'consulting_task_13_description': 'Amalda mumkin bo‘lgan yopilish birikmalari va vaqtinchalik ish tartibini aniqlash uchun '
                                          'obyektlarning yopilishi hamda ulardan foydalanish imkoniyati kamayishini baholash.',
        'consulting_task_14_title': 'Yo‘lovchilar harakati va navbatlar joylashuvi',
        'consulting_task_14_description': 'Yo‘lak kengligi, to‘siqlar, aylanma yo‘llar va navbatlar joylashuvini yurish masofasi, '
                                          'tirbandlik va kutish davomiyligi bo‘yicha solishtirib, makonni yaxshilashni tavsiya qilish.',
        'consulting_task_15_title': 'Umumiy hududga kirish va transport tutashuvlari',
        'consulting_task_15_description': 'Kelishilgan doirada yo‘lovchilar va transport kelishini, terminal oldidagi tushirish-olish '
                                          'joylari, avtoturargohlar, kirish yo‘llari va jamoat transporti tutashuvlari variantlarini '
                                          'baholash.',
        'consulting_task_16_title': 'Birgalikdagi sharoitlar va yuqori yuklama ssenariylari',
        'consulting_task_16_description': 'Zaif joylarni aniqlash, tirbandlikni kamaytirish va ishni tiklash variantlarini solishtirish '
                                          'uchun eng yuqori talab, reys kechikishlari, yopilishlar va aviakompaniya ko‘chirilishini '
                                          'birlashtirish.',
        'consulting_tab_airside': 'Aerodrom hududi',
        'consulting_airside_intro': 'Uchish-qo‘nish yo‘lagi, rullash yo‘laklari, turargohlar va yordamchi obyektlar rejalarini havo '
                                    'kemalari hamda yerusti xizmat operatsiyalari bilan birga baholash.',
        'consulting_task_17_title': 'Uchish-qo‘nish yo‘lagi quvvati va reys kechikishlari',
        'consulting_task_17_description': 'Yo‘lak o‘tkazish qobiliyati va kelish-ketish kechikishlarini, jumladan ko‘rinish past '
                                          'sharoitda, baholash uchun ish rejimlari, bandlik vaqti, ajratish intervallari va zich reys '
                                          'oqimini modellashtirish.',
        'consulting_task_18_title': 'Tezkor chiqish rullash yo‘laklarining joylashuvi',
        'consulting_task_18_description': 'Havo kemalarining qo‘nish xususiyatlari va uchish-qo‘nish yo‘lagi bandligini hisobga olib, '
                                          'tezkor chiqish yo‘laklarining o‘rni va oralig‘ini solishtirish.',
        'consulting_task_19_title': 'Aerodrom rejasi o‘zgarishlari va ta’siri',
        'consulting_task_19_description': 'Yangi, uzaytirilgan, qayta ulangan yoki yopilgan uchish-qo‘nish va rullash yo‘laklari hamda '
                                          'perronlarning yo‘nalishlar, rullash vaqti, tor joylar va operatsion to‘qnashuvlarga ta’sirini '
                                          'baholash.',
        'consulting_task_20_title': 'Turargoh taqsimoti va bir vaqtda orqaga surish',
        'consulting_task_20_description': 'Joylashuv va operatsion variantlarni tavsiya qilish uchun havo kemasi mosligi, terminalga '
                                          'tutash va uzoq turargohlar taqsimoti, bandlik hamda bir vaqtdagi harakatlarni baholash.',
        'consulting_task_21_title': 'Havo kemalari va yerusti xizmat transporti harakati',
        'consulting_task_21_description': 'Xizmat yo‘llari tirbandligi, kesishuvlardagi xalaqit va transport ish rejalarini baholash uchun '
                                          'havo kemalari harakati hamda orqaga surishni transport vazifalari va yo‘nalishlari bilan birga '
                                          'modellashtirish.',
        'consulting_task_22_title': 'Yuk perronlari va yuk samolyotlari operatsiyalari',
        'consulting_task_22_description': 'Yirik yuk samolyotlari uchun turargoh mosligi, bandligi, kirish yo‘llari va yuk terminallari '
                                          'hamda yerusti logistikasi bilan bog‘lanishni baholash.',
        'consulting_task_23_title': 'MRO, angar va GA/FBO obyektlariga kirish',
        'consulting_task_23_description': 'Havo kemasi mosligi, angarga kirish, shatakka olish yo‘llari hamda qo‘shni perron va xizmat '
                                          'yo‘llari bilan o‘zaro ta’sirni ko‘rib chiqish.',
        'consulting_task_24_title': 'Muzdan tozalash obyektlari rejasi va ishlashi',
        'consulting_task_24_description': 'Bir vaqtda qabul qilish imkoniyati, kirish-chiqish yo‘llari va havo kemalari atrofidagi xavfsiz '
                                          'oraliqlarni baholab, ishlov vaqti o‘zgarganda navbatlar va jo‘nash kechikishlarini '
                                          'solishtirish.',
        'consulting_task_25_title': 'ARFF, yoqilg‘i va yordamchi obyektlarni joylashtirish',
        'consulting_task_25_description': 'Rejalashtirish va operatsion qarorlarni qo‘llab-quvvatlash uchun qutqaruv-yong‘in xizmati, '
                                          'yoqilg‘i va kommunal obyektlar joylashuvi, kirish yo‘llari hamda xizmat qamrovini baholash.',
        'consulting_task_26_title': 'Dispetcherlik minorasidan ko‘rinish va to‘siq cheklovlari',
        'consulting_task_26_description': 'Rejalashtirish bosqichida ko‘rish chiziqlari va ko‘rinmaydigan joylarni solishtirish, '
                                          'uchish-qo‘nish yo‘lagi va atrofdagi obyektlar rejalari bilan bog‘liq to‘siqlarni cheklash '
                                          'sirtlari ustma-ust tushishini ko‘rib chiqish.',
        'consulting_tab_digital': 'Raqamli egizaklar',
        'consulting_digital_intro': 'Aeroport rivojlanish bosqichlarini modellashtirish, ish qoidalarini tekshirish va loyiha uchun zarur '
                                    'tahlil imkoniyatlarini yaratish.',
        'consulting_task_27_title': 'Hozirgi va kelajakdagi aeroport modellari',
        'consulting_task_27_description': 'Fazoviy ma’lumotlarni tayyorlash va har bosqichda rejalashtirilgan obyektlar bilan mavjud, '
                                          'ochilish, oraliq kengaytirish hamda yakuniy rivojlanish rejalarini modellashtirish.',
        'consulting_task_28_title': 'Aeroportga mos modellar va operatsion tekshiruv',
        'consulting_task_28_description': 'O‘ziga xos joylashuv, obyektlardan foydalanish qoidalari va ish tartiblarini sozlash, so‘ng '
                                          'mavjud kuzatuvlar hamda operatsion yozuvlar asosida tekshirish va kalibrlash.',
        'consulting_task_29_title': 'Loyihalarni ustma-ust ko‘rish va fazoviy tasvirlash',
        'consulting_task_29_description': 'Mavjud rejalar, variantlar va qurilish bosqichlarini solishtirish; havo kemalari, transport va '
                                          'yo‘lovchi oqimlarini reja ko‘rinishlari, fazoviy modellar hamda simulyatsiya videolari orqali '
                                          'tushuntirish.',
        'consulting_task_30_title': 'Maxsus KPI va tahlil funksiyalari',
        'consulting_task_30_description': 'Aeroportga xos ko‘rsatkichlarni, jumladan darvozalarning bir vaqtdagi ishlashi va transfer '
                                          'vaqti chegarasidan oshishlarni belgilash, zarur kirish-chiqish ma’lumotlari hamda natijalarga '
                                          'kirish funksiyalarini sozlash.',
        'consulting_scope_note': 'Ish doirasi, model tafsiloti va baholash mezonlari aeroport ma’lumotlari, ish sharoitlari hamda loyiha '
                                 'talablariga muvofiq kelishiladi. Qo‘shimcha tadqiqotlar, funksiya ishlab chiqish va tashqi tizim '
                                 'integratsiyasi zarur muddat bilan birga alohida belgilanadi.',
        'consulting_expertise_heading': 'Texnologiya va aeroport tajribasi',
        'consulting_expertise_origin': 'Team Flexa Incheon International Airport Corporation ichki tadbirkorlik dasturi doirasida '
                                       'shakllangan. Jamoamiz Incheon aeroportidagi operatsiyalarni yaxshilash va kengaytirish, shuningdek '
                                       'korporatsiyaning xorijiy aeroport faoliyati doirasidagi topshiriqlarda ishlagan.',
        'consulting_expertise_01_title': 'O‘zimiz ishlab chiqqan dasturiy ta’minot',
        'consulting_expertise_01_description': 'Dasturiy ta’minotni o‘zimiz ishlab chiqamiz va unga egalik qilamiz. Model hamda '
                                               'funksiyalarni tadqiqotga moslab, alohida tahlil vositalari yoki maxsus xodimlarga '
                                               'ehtiyojni kamaytiramiz.',
        'consulting_expertise_02_title': 'Maxsus KPI va tahlil funksiyalari',
        'consulting_expertise_02_description': 'Sizning samaradorlik ko‘rsatkichlaringiz, baholash mezonlaringiz va hisobot '
                                               'shakllaringizdan foydalanamiz; mavjud funksiyalar yetarli bo‘lmasa, qo‘shimcha ishlab '
                                               'chiqish yoki integratsiyani kelishamiz.',
        'consulting_expertise_03_title': 'Aeroportga xos qoidalar va rejalar',
        'consulting_expertise_03_description': 'Terminallar bog‘lanishi, aviakompaniyalarning obyektlardan foydalanish qoidalari, turargoh '
                                               'konfiguratsiyasi, yerusti xizmat yo‘nalishlari va vaqtga bog‘liq cheklovlarni '
                                               'modellashtiramiz.',
        'consulting_expertise_04_title': 'Mavjud ma’lumotlar va modellar',
        'consulting_expertise_04_description': 'Tayyorlash vaqtini qisqartirish uchun mavjud aeroport, parvoz va obyekt ma’lumotlari hamda '
                                               'modellardan foydalanamiz; ularni kuzatuvlaringiz va kelishilgan mezonlar bilan '
                                               'tekshiramiz.',
        'consulting_expertise_05_title': 'Bog‘langan havo kemasi, transport va yo‘lovchi oqimlari',
        'consulting_expertise_05_description': 'Havo kemalari harakati va transport vazifalari birgalikda modellashtiriladi. Darvozalar '
                                               'taqsimoti va yo‘lovchilar kelishi aerodrom hamda terminal tadqiqotlarini bog‘lab, obyekt '
                                               'o‘zgarishlarining kengroq ta’sirini baholashga yordam beradi.',
        'consulting_engagements_heading': 'Biz bilan hamkorlik',
        'consulting_engagements_terms': 'Faqat konsalting yoki tanlangan dasturiy funksiyalar va litsenziyalar bilan konsalting xizmatlari '
                                        'mavjud. Natijalarga bevosita kirish, keyingi ko‘rib chiqish funksiyalari va ulardan foydalanish '
                                        'shartlari alohida kelishiladi.',
        'consulting_engagements_01_title': 'Loyiha bo‘yicha konsalting',
        'consulting_engagements_01_application': 'Aeroportni kengaytirish, aviakompaniyalarni ko‘chirish, qurilish rejalari va boshqa aniq '
                                                 'rejalashtirish ehtiyojlari.',
        'consulting_engagements_01_role': 'Modellar yaratamiz, variantlarni solishtiramiz va yaxshilash choralarini tavsiya qilamiz; '
                                          'natijalarni rejalashtirish va budjet ko‘rib chiqishlari uchun tayyorlaymiz.',
        'consulting_engagements_02_title': 'Qo‘shma takliflar va loyihani bajarish',
        'consulting_engagements_02_application': 'Loyihalash, muhandislik va konsalting topshiriqlaridagi simulyatsiya hamda o‘tkazish '
                                                 'qobiliyatini baholash.',
        'consulting_engagements_02_role': 'Taklif bosqichida usul, mas’uliyat, jadval va haqni kelishamiz; shartnoma olingach, loyihalarni '
                                          'tekshirish hamda variantlarni solishtirish uchun kelishilgan tahlilni bajaramiz.',
        'consulting_engagements_03_title': 'Doimiy texnik hamkorlik',
        'consulting_engagements_03_application': 'Bir nechta aeroport loyihasi bo‘yicha maxsus tahlil.',
        'consulting_engagements_03_role': 'Kelishilgan davr davomida loyiha ko‘rigi, ssenariy tahlili va texnik maslahat beramiz; buning '
                                          'uchun alohida ichki tahlil guruhi talab qilinmaydi.',
        'consulting_deliverables_heading': 'Topshiriladigan natijalar',
        'consulting_deliverables_usage_rights': 'Taqdim etilgan ma’lumotlar, modellar, hisoblar yoki yechim funksiyalaridan foydalanish '
                                                'huquqi va muddati hamkorlik shartlarida belgilanadi.',
        'consulting_deliverables_01_title': 'Konsalting hisobotlari',
        'consulting_deliverables_01_use': 'Maqsadlar, variantlar bahosi, tavsiyalar va investitsiya ustuvorliklarini qamrab olgan texnik '
                                          'hisobotlar yoki rahbariyat uchun qisqa xulosalar.',
        'consulting_deliverables_02_title': 'HTML veb-hisobotlar',
        'consulting_deliverables_02_use': 'Ssenariylar, solishtirishlar va fazoviy tasvirlarni brauzer orqali ko‘rib chiqish.',
        'consulting_deliverables_03_title': 'PDF va DOCX',
        'consulting_deliverables_03_use': 'Loyiha hujjatlarini topshirish, ichki ko‘rib chiqish, birgalikda tahrirlash va bosma tarqatish.',
        'consulting_deliverables_04_title': 'Videolar va render tasvirlar',
        'consulting_deliverables_04_use': 'Yig‘ilishlar va manfaatdor tomonlar bilan muloqot uchun simulyatsiya videolari, muqobil rejalar '
                                          'solishtiruvi va fazoviy tasvirlar.',
        'consulting_deliverables_05_title': 'Ma’lumotlar, modellar va tanlangan yechim qismlari',
        'consulting_deliverables_05_use': 'Hamkorlik doirasida kelishilgan ma’lumotlar to‘plamlari, model paketlari, kirish hisoblari yoki '
                                          'funksiyalar.',
        'consulting_programme_heading': 'Ish jadvali va haq',
        'consulting_programme_01_title': 'Loyihaga mos ish jadvali',
        'consulting_programme_01_description': 'Ish jadvalini loyiha muddatlaringizga moslaymiz; tadqiqot doirasi, ma’lumot tayyorlash, '
                                               'modelni tekshirish va ko‘rib chiqishlar hisobga olinadi.',
        'consulting_programme_02_title': 'Belgilangan muddatga yordam',
        'consulting_programme_02_description': 'Loyiha ko‘rigi, ssenariy tahlili va texnik maslahat kelishilgan davrlarga, masalan bir, '
                                               'uch yoki olti oyga beriladi; ish hajmi, takrorlanish va javob muddatlari alohida '
                                               'kelishiladi.',
        'consulting_programme_03_title': 'Bosqichma-bosqich bajarish',
        'consulting_programme_03_description': 'Konsepsiya, dastlabki loyiha, batafsil loyiha va qurilish bosqichlarida tadqiqot buyurtma '
                                               'qilish, rejalar o‘zgarganda qo‘shimcha ko‘rib chiqishlar o‘tkazish.',
        'consulting_programme_04_title': 'Narxlash',
        'consulting_programme_04_description': 'Haq ish doirasi, loyiha ko‘lami, davomiyligi, muqobil variantlar soni va maxsus ishlab '
                                               'chiqish talablariga qarab belgilanadi.',
        'footer_copyright': 'Mualliflik huquqi 2026 TeamFlexa CO., LTD. Barcha huquqlar himoyalangan.',
        'flexa_about_title': 'Flexa haqida',
        'flexa_about_p1': 'Flexa — aeroport yechimlariga ixtisoslashgan TeamFlexa CO., LTD. kompaniyasining brendi. Kompaniya ma’lumotlar '
                          'orqali aeroport faoliyatidagi murakkabliklarni ochib beradi hamda simulyatsiya texnologiyalari va sun’iy '
                          'intellektga asoslangan tahlil yordamida optimal natijalarga erishadi. Biz tahlil bilan cheklanmay, faoliyatni '
                          'amalda yaxshilashga xizmat qiladigan aniq tavsiyalarni taqdim etamiz.',
        'flexa_about_p2': 'Incheon xalqaro aeroportida ichki startap sifatida tashkil etilgan TeamFlexa dunyoning yetakchi aeroportlaridan '
                          'birida to‘plangan tajriba va ma’lumotlardan foydalanadi. Flexa brendi ostida terminal faoliyatini '
                          'optimallashtirishdan tortib o‘rta va uzoq muddatli infratuzilma strategiyasigacha kompleks konsalting va '
                          'yechimlarni taklif etamiz. Bu mijozlarga murakkab muammolarni miqdoriy ifodalash va eng samarali qarorlarni '
                          'qabul qilish imkonini beradi.',
        'flexa_about_p3': 'TeamFlexa butun dunyodagi aeroportlar, aeroport operatorlari hamda muhandislik va qurilish kompaniyalariga '
                          'xizmat ko‘rsatadi. Biz muammolarni tez va aniq aniqlaymiz, ehtiyojga mos strategiyalarni ishlab chiqamiz va '
                          'ularning amalga oshirilishini ta’minlaymiz. Aeroport faoliyati standartlarini yangicha belgilab, global bozorda '
                          'ma’lumotlarga asoslangan qarorlar qabul qilish bo‘yicha yetakchi hamkor sifatida faoliyat yuritamiz.'},
 'kk': {'consulting_eyebrow': 'Консалтингтік қызметтер',
        'consulting_heading': 'Әуежай консалтингі',
        'consulting_intro': 'Әуежайлар мен инженерлік топтарға арналған жоспарлау, модельдеу және техникалық қолдау.',
        'consulting_projects_heading': 'Жобаларда қолдану',
        'consulting_tab_overall': 'Жалпы шолу',
        'consulting_tabs_aria': 'Консалтинг бағыттары',
        'consulting_overall_intro': 'Негізгі жобаларға жаңа әуежайлар мен терминалдар, кеңейту, жұмысты тоқтатпай жаңарту, әуе '
                                    'компанияларын немесе нысандарды көшіру, кезеңдік инвестициялар және операцияларды жетілдіру кіреді.',
        'consulting_overall_01_title': 'Әуе компанияларын көшіру',
        'consulting_overall_01_role': 'Тіркеу, қауіпсіздік тексеруі және трансферлік жолаушыларға қызмет көрсету нысандары көшірілетін әуе '
                                      'компанияларын қабылдай ала ма — соны бағалап, қолайлы жоспарлау нұсқаларын салыстыру.',
        'consulting_overall_02_title': 'Жаңа терминалдар және әуежайды кеңейту',
        'consulting_overall_02_role': 'Ашылу мерзімдерін, нысандардың өлшемдерін және жаңа әрі қолданыстағы терминалдар арасындағы '
                                      'міндеттер бөлінісін салыстыру.',
        'consulting_overall_03_title': 'Әуеайлақ жоспарын өзгерту',
        'consulting_overall_03_role': 'Рульдеу жолдары мен тұрақ орындарындағы өзгерістер әуе кемелерінің қозғалысына және жерде қызмет '
                                      'көрсететін көлік ағындарына қалай әсер ететінін бағалау.',
        'consulting_overall_04_title': 'Жұмысты тоқтатпай жаңарту',
        'consulting_overall_04_role': 'Қай нысандарды бір уақытта жабуға болатынын бағалап, уақытша бағыттар мен құрылыс жұмыстарының '
                                      'кезектілігін салыстыру.',
        'consulting_overall_05_title': 'Бірлескен жобалау және инженерлік ұсыныстар',
        'consulting_overall_05_role': 'Ұсыныстарды әзірлеуге модельдеу және өткізу қабілетін бағалау жөніндегі техникалық серіктес ретінде '
                                      'қатысып, келісімшарт алынғаннан кейін келісілген талдауды орындау.',
        'consulting_overall_06_title': 'Әуежайды дамыту стратегиясы',
        'consulting_overall_06_role': 'Инвестиция мерзімдері мен нысан өлшемдерін негіздеу үшін сұранысты, өткізу қабілетін және '
                                      'баламаларды бағалау.',
        'consulting_tab_demand': 'Сұраныс және ұшу кестелері',
        'consulting_demand_intro': 'Болашақ сұранысты жұмыс сценарийлеріне, нысандарға қойылатын талаптарға және кеңейту жөніндегі '
                                   'шешімдерге айналдыру.',
        'consulting_task_01_title': 'Болашақ тасымал көлемі және жолаушылар сұранысы',
        'consulting_task_01_description': 'Нысандар мен операцияларға қойылатын талаптарды бағалау үшін қолданыстағы болжамдар мен '
                                          'пайдалану деректері негізінде есептік жылға және өсу кезеңдеріне арналған сценарийлер әзірлеу.',
        'consulting_task_02_title': 'Есептік күн мен ең жоғары жүктемелі сағаттағы сұраныс',
        'consulting_task_02_description': 'Нысандар көтеруге тиіс жүктемені анықтау үшін жылдық сұранысты әдеттегі күн, ең жүктелген күн '
                                          'және сағаттық сұраныс профильдеріне түрлендіру.',
        'consulting_task_03_title': 'Болашақ ұшу кестелерін әзірлеу',
        'consulting_task_03_description': 'Сұраныс, әуе кемелері паркінің құрамы, әуе компанияларының жұмыс ерекшеліктері және жұмыс '
                                          'уақыты негізінде есептік күнге арналған кестелер құрып, олардың іс жүзінде орындалу мүмкіндігін '
                                          'бағалау.',
        'consulting_task_04_title': 'Әуе кемелері паркінің құрамы және әуе компанияларының жұмыс ерекшеліктері',
        'consulting_task_04_description': 'Әуе кемелерінің өлшемдері, әуе компаниялары мен бағыттардың құрамы, сондай-ақ келу мен ұшудың '
                                          'шоғырланған кезеңдері отырғызу қақпаларына, тұрақ орындарына және терминалдарға деген сұранысқа '
                                          'қалай әсер ететінін салыстыру.',
        'consulting_task_05_title': 'Жолаушылар санаттары және келу профильдері',
        'consulting_task_05_description': 'Әуежайға келу тәртібі мен отырғызу қақпаларының бөлінуін ескере отырып, ұшатын, келетін және '
                                          'трансферлік жолаушылардың нысандарға қашан және қай жерден келетінін модельдеу.',
        'consulting_task_06_title': 'Өткізу қабілетінің тапшылығы және кеңейту шарттары',
        'consulting_task_06_description': 'Кеңейту шектерін, болжамды мерзімдерді және нысандардың басымдығын ұсыну үшін өсіп жатқан '
                                          'сұранысты өткізу қабілетінің шектерімен және қалған резервімен салыстыру.',
        'consulting_tab_terminal': 'Терминал және кіреберіс аумақ',
        'consulting_terminal_intro': 'Жолаушыларға қызмет көрсету үдерістерін, нысандардың орналасуын, әуе компанияларын көшіруді, құрылыс '
                                     'кезеңдерін және қатынау жолдарын бағалау.',
        'consulting_task_07_title': 'Терминал нысандарының өлшемдері мен жеткіліктілігі',
        'consulting_task_07_description': 'Қажетті нысандар санын және жұмыс уақытын анықтау үшін қызмет көрсету орындары мен күту '
                                          'аймақтарын сұранысқа және қызмет сапасы өлшемшарттарына сәйкес бағалау.',
        'consulting_task_08_title': 'Ұшу алдындағы үдерістер және жұмыс жоспарлары',
        'consulting_task_08_description': 'Тіркеу, багажды өздігінен тапсыру, отырғызу талондарын тексеру, қауіпсіздік тексеруі және ұшу '
                                          'алдындағы шекаралық бақылау үшін нысандарды ашу тәртібін, жұмыс уақытын және қызметкерлер санын '
                                          'салыстыру.',
        'consulting_task_09_title': 'Келу, багаж алу және кеден',
        'consulting_task_09_description': 'Бір кезеңдегі өзгерістердің жалпы қызмет көрсету уақытына және кейінгі кезеңдердегі жүктемеге '
                                          'әсерін бағалау үшін келу кезіндегі шекаралық бақылауды, багаж алуды және кедендік бақылауды '
                                          'бірге модельдеу.',
        'consulting_task_10_title': 'Трансферлік ағындар және терминалдар арасындағы байланыс',
        'consulting_task_10_description': 'Трансферлік қауіпсіздік тексеруінде, отырғызу қақпалары арасындағы жолдарда, дәліздерде және '
                                          'терминалараралық көлік платформаларында кептеліс пен ауысып міну уақытын бағалау.',
        'consulting_task_11_title': 'Әуе компанияларын көшіру және нысандарға әсері',
        'consulting_task_11_description': 'Әуе компанияларын терминалдар, галереялар, тіркеу аймақтары немесе отырғызу қақпалары арасында '
                                          'көшіру нұсқаларын жолаушылардың бөлінуі, нысандар жүктемесі, трансферлік бағыттар және отырғызу '
                                          'залдарының толуы бойынша салыстыру.',
        'consulting_task_12_title': 'Жаңа терминалдар және кезеңдік кеңейту',
        'consulting_task_12_description': 'Ашылу сәтіндегі және кейінгі кеңейту кезеңдеріндегі өткізу қабілетін бағалау үшін нысандардың '
                                          'өлшемдерін, орналасуын, қызметтерін және қолданыстағы терминалдармен байланысын салыстыру.',
        'consulting_task_13_title': 'Әуежай жұмысын тоқтатпай жаңарту',
        'consulting_task_13_description': 'Нысандарды жабудың іске асатын үйлесімдерін және уақытша жұмыс тәртібін анықтау үшін '
                                          'жабылуларды және нысандардың қолжетімділігінің азаюын бағалау.',
        'consulting_task_14_title': 'Жолаушылар қозғалысы және кезектерді орналастыру',
        'consulting_task_14_description': 'Дәліз енін, қалқаларды, айналма жолдарды және кезек сызбаларын жүру қашықтығы, кептеліс және '
                                          'болу ұзақтығы бойынша салыстырып, кеңістікті жоспарлауды жақсарту жөнінде ұсыныстар беру.',
        'consulting_task_15_title': 'Жерүсті қатынасы және көлік байланыстары',
        'consulting_task_15_description': 'Келісілген жұмыс көлемі аясында жолаушылар мен көліктің келуін, терминал алдындағы мінгізу және '
                                          'түсіру аймақтарының, автотұрақтардың, кірме жолдардың және қоғамдық көлік түйіндерінің орналасу '
                                          'нұсқаларын бағалау.',
        'consulting_task_16_title': 'Біріккен жағдайлар және жоғары жүктеме сценарийлері',
        'consulting_task_16_description': 'Осал аймақтарды анықтап, кептелісті азайту және жұмысты қалпына келтіру нұсқаларын салыстыру '
                                          'үшін ең жоғары сұранысты, рейс кідірістерін, нысандардың жабылуын және әуе компанияларын '
                                          'көшіруді бірге қарастыру.',
        'consulting_tab_airside': 'Әуеайлақ',
        'consulting_airside_intro': 'Ұшу-қону жолақтарының, рульдеу жолдарының, тұрақ орындарының және қосалқы нысандардың жоспарларын әуе '
                                    'кемелерінің қозғалысымен және жерде қызмет көрсету операцияларымен бірге бағалау.',
        'consulting_task_17_title': 'ҰҚЖ өткізу қабілеті және рейс кідірістері',
        'consulting_task_17_description': 'Көру мүмкіндігі төмен жағдайларды қоса алғанда, жолақтың өткізу қабілетін және келу мен ұшу '
                                          'кідірістерін бағалау үшін жұмыс режимдерін, жолақтың бос болмау уақытын, эшелондау аралықтарын '
                                          'және қозғалыстың шоғырлануын модельдеу.',
        'consulting_task_18_title': 'Жолақтан жылдам шығу жолдарының орны мен жоспары',
        'consulting_task_18_description': 'Әуе кемелерінің қону сипаттамаларын және ұшу-қону жолағының бос болмау уақытын ескере отырып, '
                                          'жылдам шығу рульдеу жолдарының орналасуын және арақашықтығын салыстыру.',
        'consulting_task_19_title': 'Әуеайлақ жоспарын өзгерту және оның әсері',
        'consulting_task_19_description': 'Жаңа, ұзартылған, байланысы өзгертілген немесе жабылған ұшу-қону жолақтары, рульдеу жолдары мен '
                                          'перрондар бағыттарға, рульдеу уақытына, тар орындарға және операциялар кезіндегі өзара '
                                          'кедергілерге қалай әсер ететінін бағалау.',
        'consulting_task_20_title': 'Тұрақ орындарын бөлу және бір мезгілде кері сүйреу',
        'consulting_task_20_description': 'Жоспарлау және жұмыс нұсқаларын ұсыну үшін әуе кемелерінің сәйкестігін, терминалға жалғасқан '
                                          'және қашықтағы тұрақ орындарының бөлінуін, олардың бос болмауын және бір мезгілдегі '
                                          'қозғалыстарды бағалау.',
        'consulting_task_21_title': 'Әуе кемелері мен жерде қызмет көрсету көлігінің қозғалысы',
        'consulting_task_21_description': 'Қызметтік жолдардағы кептелісті, қиылыстардағы өзара кедергілерді және көліктің жұмыс '
                                          'жоспарларын бағалау үшін әуе кемелерінің қозғалысы мен кері сүйрелуін көлік міндеттерімен және '
                                          'бағыттарымен бірге модельдеу.',
        'consulting_task_22_title': 'Жүк перрондары және жүк әуе кемелерінің жұмысы',
        'consulting_task_22_description': 'Тұрақ орындарының ірі жүк әуе кемелеріне сәйкестігін, олардың бос болмауын, қатынау бағыттарын '
                                          'және жүк терминалдары мен жерүсті логистикасымен байланысын бағалау.',
        'consulting_task_23_title': 'MRO, ангарлар және GA/FBO нысандарына қатынау',
        'consulting_task_23_description': 'Әуе кемелерінің сәйкестігін, ангарларға кіру мүмкіндігін, сүйреу бағыттарын және іргелес '
                                          'перрондармен әрі қызметтік жолдармен өзара ықпалын тексеру.',
        'consulting_task_24_title': 'Мұздануға қарсы өңдеу алаңдарының жоспары мен жұмысы',
        'consulting_task_24_description': 'Әуе кемелерін бір мезгілде орналастыруды, кіру және шығу бағыттарын, қауіпсіз арақашықтықтарды '
                                          'бағалап, өңдеу ұзақтығы өзгерген кезде кезектер мен ұшу кідірістерін салыстыру.',
        'consulting_task_25_title': 'ARFF, отын және қосалқы нысандарды орналастыру',
        'consulting_task_25_description': 'Жоспарлау және жұмыс жөніндегі шешімдерді негіздеу үшін авариялық-құтқару және өрт сөндіру, '
                                          'отын және инженерлік нысандардың орналасуын, оларға қатынау жолдарын және қызмет көрсету '
                                          'аумақтарын бағалау.',
        'consulting_task_26_title': 'Диспетчерлік мұнарадан көріну және кедергілерге қойылатын шектеулер',
        'consulting_task_26_description': 'Шолу бағыттары мен көрінбейтін аймақтарды салыстырып, жоспарлау кезеңінде ұшу-қону жолақтары '
                                          'мен айналадағы нысандар жоспарларына байланысты кедергілерді шектеу беттерімен қиылысуларды '
                                          'тексеру.',
        'consulting_tab_digital': 'Цифрлық егіздер',
        'consulting_digital_intro': 'Әуежайдың даму кезеңдерін модельдеу, жұмыс ережелерін тексеру және жобаға қажетті талдау '
                                    'мүмкіндіктерін әзірлеу.',
        'consulting_task_27_title': 'Әуежайдың қазіргі және болашақ модельдері',
        'consulting_task_27_description': 'Кеңістіктік бастапқы деректерді дайындап, әр кезеңге жоспарланған нысандармен бірге '
                                          'қолданыстағы, ашылу кезіндегі, аралық кеңейту және түпкілікті даму жоспарларын модельдеу.',
        'consulting_task_28_title': 'Әуежай ерекшеліктеріне сай модельдер және жұмысқа жарамдылығын тексеру',
        'consulting_task_28_description': 'Ерекше жоспарларды, нысандарды пайдалану ережелерін және жұмыс рәсімдерін баптап, қолда бар '
                                          'бақылаулар мен пайдалану жазбалары бойынша модельдерді тексеру және калибрлеу.',
        'consulting_task_29_title': 'Жобаларды қабаттастыру және кеңістіктік визуализация',
        'consulting_task_29_description': 'Қолданыстағы жоспарларды, баламаларды және құрылыс кезеңдерін салыстырып, әуе кемелері, көлік '
                                          'және жолаушылар ағындарын жоспарлар, кеңістіктік модельдер және модельдеу бейнелері арқылы '
                                          'түсіндіру.',
        'consulting_task_30_title': 'Арнайы KPI және талдау функциялары',
        'consulting_task_30_description': 'Отырғызу қақпаларындағы бір мезгілдегі операциялар мен ауысып міну уақытының асып кетуін қоса '
                                          'алғанда, әуежайға тән көрсеткіштерді анықтап, қажетті кіріс деректерін, шығыс нәтижелерін және '
                                          'оларға қол жеткізу функцияларын баптау.',
        'consulting_scope_note': 'Жұмыс көлемі, модельдің егжей-тегжейлілігі және бағалау өлшемшарттары әуежай деректеріне, пайдалану '
                                 'жағдайларына және жоба талаптарына сай келісіледі. Қосымша зерттеулер, функцияларды әзірлеу және сыртқы '
                                 'жүйелермен біріктіру көлемі қажетті мерзімдермен бірге анықталады.',
        'consulting_expertise_heading': 'Технологиялар және әуежайлармен жұмыс тәжірибесі',
        'consulting_expertise_origin': 'Team Flexa Incheon International Airport Corporation ішкі кәсіпкерлік бағдарламасынан бастау алды. '
                                       'Біздің команда Инчхон әуежайының операцияларын жетілдіру және оны кеңейту жұмыстарымен, сондай-ақ '
                                       'корпорацияның шетелдік әуежай жобаларымен айналысты.',
        'consulting_expertise_01_title': 'Өзіміз әзірлеген бағдарламалық қамтылым',
        'consulting_expertise_01_description': 'Біз бағдарламалық қамтылымды өзіміз әзірлейміз және оған иелік етеміз, модельдер мен '
                                               'функцияларды зерттеуге бейімдеп, бөлек талдау құралдарына немесе арнайы мамандарға деген '
                                               'қажеттілікті азайтамыз.',
        'consulting_expertise_02_title': 'Арнайы KPI және талдау функциялары',
        'consulting_expertise_02_description': 'Біз сіздің тиімділік көрсеткіштеріңізді, бағалау өлшемшарттарыңызды және есеп '
                                               'пішімдеріңізді қолданамыз; қолданыстағы функциялар жеткіліксіз болса, қосымша әзірлеуді '
                                               'немесе жүйелерді біріктіруді келісеміз.',
        'consulting_expertise_03_title': 'Әуежайға тән ережелер мен жоспарлар',
        'consulting_expertise_03_description': 'Біз терминалдар арасындағы байланыстарды, әуе компанияларының нысандарды пайдалану '
                                               'ережелерін, тұрақ орындарының конфигурацияларын, жерде қызмет көрсету бағыттарын және '
                                               'уақытқа байланысты шектеулерді модельдейміз.',
        'consulting_expertise_04_title': 'Қолда бар деректер мен модельдер',
        'consulting_expertise_04_description': 'Дайындық уақытын қысқарту үшін әуежай, рейстер және нысандар жөніндегі қолда бар деректер '
                                               'мен модельдерді пайдаланамыз және оларды сіздің бақылауларыңыз бен келісілген өлшемшарттар '
                                               'бойынша тексереміз.',
        'consulting_expertise_05_title': 'Әуе кемелері, көлік және жолаушылар ағындарының байланысы',
        'consulting_expertise_05_description': 'Әуе кемелерінің қозғалысы мен көлік міндеттері бірге модельденеді; отырғызу қақпаларының '
                                               'бөлінуі және жолаушылардың келуі әуеайлақ пен терминал зерттеулерін байланыстырып, нысан '
                                               'өзгерістерінің кең ауқымды әсерін бағалауға мүмкіндік береді.',
        'consulting_engagements_heading': 'Бізбен жұмыс істеу',
        'consulting_engagements_terms': 'Қызметтер тек консалтинг түрінде немесе таңдалған бағдарламалық функциялармен не лицензиялармен '
                                        'бірге ұсынылады. Нәтижелерге немесе кейінгі талдау функцияларына тікелей қол жеткізу және оларды '
                                        'пайдалану шарттары бөлек келісіледі.',
        'consulting_engagements_01_title': 'Жоба бойынша консалтинг',
        'consulting_engagements_01_application': 'Әуежайды кеңейту, әуе компанияларын көшіру, құрылыс жоспарлары және басқа да нақты '
                                                 'жоспарлау міндеттері.',
        'consulting_engagements_01_role': 'Біз модельдер әзірлейміз, нұсқаларды салыстырамыз және жақсарту шараларын ұсынамыз; нәтижелерді '
                                          'жоспарлар мен бюджеттерді қарауға дайындаймыз.',
        'consulting_engagements_02_title': 'Бірлескен ұсыныстар және жобаларды орындау',
        'consulting_engagements_02_application': 'Жобалау, инженерлік және консалтингтік жұмыстар аясындағы модельдеу және өткізу '
                                                 'қабілетін бағалау.',
        'consulting_engagements_02_role': 'Ұсыныс кезеңінде әдісті, міндеттерді, кестені және қызмет құнын келісеміз; келісімшарт '
                                          'алынғаннан кейін жобалық шешімдерді тексеріп, баламаларды салыстыру үшін келісілген талдауды '
                                          'орындаймыз.',
        'consulting_engagements_03_title': 'Тұрақты техникалық серіктестік',
        'consulting_engagements_03_application': 'Бірнеше әуежай жобасына арналған мамандандырылған талдау.',
        'consulting_engagements_03_role': 'Келісілген мерзім ішінде жобалық шешімдерді тексеру, сценарийлерді талдау және техникалық кеңес '
                                          'беру қызметтерін ұсынамыз; бұл үшін арнайы ішкі талдау тобын құру қажет емес.',
        'consulting_deliverables_heading': 'Тапсырылатын нәтижелер',
        'consulting_deliverables_usage_rights': 'Берілетін деректерді, модельдерді, есептік жазбаларды немесе шешім функцияларын пайдалану '
                                                'құқықтары мен мерзімдері әр келісім бойынша анықталады.',
        'consulting_deliverables_01_title': 'Консалтингтік есептер',
        'consulting_deliverables_01_use': 'Мақсаттар, нұсқаларды бағалау, ұсыныстар және инвестициялық басымдықтар қамтылған техникалық '
                                          'есептер немесе басшылыққа арналған қысқаша қорытындылар.',
        'consulting_deliverables_02_title': 'HTML веб-есептері',
        'consulting_deliverables_02_use': 'Сценарийлерді, салыстыруларды және кеңістіктік визуализацияларды браузерде қарау.',
        'consulting_deliverables_03_title': 'PDF және DOCX',
        'consulting_deliverables_03_use': 'Жоба құжаттарын тапсыру, ішкі қарау, бірлесіп өңдеу және баспа түрінде тарату.',
        'consulting_deliverables_04_title': 'Бейнелер және визуализациялар',
        'consulting_deliverables_04_use': 'Кеңестер мен мүдделі тараптармен байланыс үшін модельдеу бейнелері, балама жоспарларды '
                                          'салыстыру және кеңістіктік визуализациялар.',
        'consulting_deliverables_05_title': 'Деректер, модельдер және шешімнің таңдалған құрамдастары',
        'consulting_deliverables_05_use': 'Келісім аясында берілетін келісілген деректер жиындары, модель пакеттері, қол жеткізу есептік '
                                          'жазбалары немесе функциялар.',
        'consulting_programme_heading': 'Жұмыс мерзімдері және қызмет құны',
        'consulting_programme_01_title': 'Жобаға сай жұмыс кестесі',
        'consulting_programme_01_description': 'Зерттеу көлемін, деректерді дайындауды, модельді тексеруді және нәтижелерді қарауды ескере '
                                               'отырып, жұмыс кестесін сіздің жобаңыздың мерзімдеріне сәйкестендіреміз.',
        'consulting_programme_02_title': 'Белгіленген мерзімге қолдау',
        'consulting_programme_02_description': 'Жобалық шешімдерді тексеру, сценарийлерді талдау және техникалық кеңес беру келісілген '
                                               'мерзімдерге, мысалы бір, үш немесе алты айға ұсынылады; жұмыс көлемі, жиілігі және жауап '
                                               'беру мерзімдері бөлек келісіледі.',
        'consulting_programme_03_title': 'Кезеңдік орындау',
        'consulting_programme_03_description': 'Тұжырымдама, алдын ала жобалау, егжей-тегжейлі жобалау және құрылыс кезеңдерінде '
                                               'зерттеулерге тапсырыс беріп, жоспарлар өзгерген сайын қосымша тексерулер жүргізіңіз.',
        'consulting_programme_04_title': 'Қызмет құны',
        'consulting_programme_04_description': 'Қызмет құны жұмыс көлеміне, жоба ауқымына, ұзақтығына, баламалар санына және арнайы '
                                               'әзірлеу талаптарына байланысты.',
        'footer_copyright': 'Copyright 2026 TeamFlexa CO., LTD. Барлық құқықтар қорғалған.',
        'flexa_about_title': 'Flexa туралы',
        'flexa_about_p1': 'Flexa — әуежайларға арналған шешімдерге маманданған TeamFlexa CO., LTD. компаниясының бренді. Компания деректер '
                          'арқылы әуежай операцияларының күрделі байланыстарын ашып, модельдеу технологиялары мен жасанды интеллектке '
                          'негізделген талдау көмегімен оңтайлы нәтижелерге қол жеткізеді. Біз талдаумен шектелмей, операцияларды іс '
                          'жүзінде жақсартуға мүмкіндік беретін нақты қорытындылар ұсынамыз.',
        'flexa_about_p2': 'TeamFlexa Инчхон халықаралық әуежайындағы ішкі венчурлық жоба ретінде құрылып, әлемдегі жетекші әуежайлардың '
                          'бірінің тәжірибесі мен деректеріне сүйенеді. Flexa брендімен терминал жұмысын оңтайландырудан бастап '
                          'инфрақұрылымның орта және ұзақ мерзімді стратегиясына дейін кешенді консалтинг пен шешімдер ұсынамыз. Бұл '
                          'клиенттерге күрделі міндеттерді сандық тұрғыдан анықтап, ең тиімді шешімдер қабылдауға мүмкіндік береді.',
        'flexa_about_p3': 'Әлемнің түкпір-түкпіріндегі әуежайларға, әуежай операторларына, инженерлік және құрылыс компанияларына қызмет '
                          'көрсететін TeamFlexa мәселелерді жылдам әрі дәл анықтайды, жеке қажеттіліктерге сай стратегиялар әзірлейді және '
                          'олардың орындалуын қамтамасыз етеді. Біз әуежай жұмысының стандарттарын жаңаша қалыптастырып, жаһандық нарықта '
                          'деректерге негізделген шешім қабылдаудың жетекші серіктесі ретінде әрекет етеміз.'}}
